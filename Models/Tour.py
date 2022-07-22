from typing import List, Tuple

import jdatetime
from pyodbc import Row

from Models.DatabaseManager import DatabaseManager
from datetime import datetime


class TourStatus:
    NotConfirmed = 'تایید نشده'
    Registering = 'در حال ثبت نام'
    FullCapacity = 'تکمیل ظرفیت'
    Ended = 'برگزار شده'
    Canceled = 'حذف شده'


class Tour:
    def __init__(self, Id: int, destination: str, origin: str, capacity: int, departTime: jdatetime.datetime, returnTime: jdatetime.datetime, status: str, passengers: list = None, cars: list = None):
        self.id = Id
        self.destination = destination
        self.origin = origin
        self.capacity = capacity if capacity > 0 else 0
        self.departTime = departTime
        self.returnTime = returnTime
        self.status = status
        self.passengers = list()
        if passengers is not None:
            for p in passengers:
                self.passengers.append(p)

        self.cars = list()
        if cars is not None:
            for c in cars:
                self.cars.append(c)

    @classmethod
    def CreateTour(cls, destination: str, origin: str, capacity: int, departTime: datetime, returnTime: datetime) -> bool:
        try:
            cursor = DatabaseManager.execute(
                """INSERT INTO [TourTBL]
                ([Destination], [Origin], [Capacity], [DepartTime], [ReturnTime], [Status])
                VALUES 
                (?, ?, ?, ?, ?, ?)""",
                destination, origin, capacity, departTime, returnTime, TourStatus.NotConfirmed
            )
            return cursor.rowcount == 1
        except:
            return False

    @classmethod
    def DeleteTours(cls, Id: List[int]) -> bool:
        try:
            cursor = DatabaseManager.execute(
                f"UPDATE [TourTBL] SET [Status] = ? WHERE [Id] IN ({','.join('?' for _ in range(len(Id)))})",
                TourStatus.Canceled, *Id
            )
            return cursor.rowcount == len(Id)
        except Exception as e:
            print(e)
            return False

    @classmethod
    def hasTourInterference(cls, destination: str, origin: str, departTime: datetime, returnTime: datetime) -> bool:
        try:
            cursor = DatabaseManager.query(
                """SELECT COUNT(*) FROM [TourTBL] 
                WHERE [Destination] = ? AND [Origin] = ? AND (([DepartTime] <= ? AND [ReturnTime] >= ?) OR ([DepartTime] <= ? AND [ReturnTime] >= ?))""",
                destination, origin, departTime, departTime, returnTime, returnTime
            )
            return cursor.fetchone()[0] > 0
        except:
            return False

    @classmethod
    def hasPassengerInterference(cls, passenger_id: str, departTime: datetime, returnTime: datetime) -> bool:
        try:
            cursor = DatabaseManager.query(
                """SELECT p.[PassengerId]
                FROM [TourPassengersTBL] AS p
                INNER JOIN [TourTBL] AS t
                ON p.TourId = t.Id
                WHERE p.[PassengerId] = ? AND ((t.[DepartTime] <= ? AND t.[ReturnTime] >= ?) OR (t.[DepartTime] <= ? AND t.[ReturnTime] >= ?))""",
                passenger_id, departTime, departTime, returnTime, returnTime
            )
            return len(cursor.fetchall()) > 0
        except:
            return False

    @classmethod
    def hasCarInterference(cls, car_id: int, departTime: datetime, returnTime: datetime) -> bool:
        try:
            cursor = DatabaseManager.query(
                """SELECT c.[CarId]
                FROM [TourCarsTBL] AS c
                INNER JOIN [TourTBL] AS t on t.Id = c.TourId
                WHERE c.[CarId] = ? AND (([DepartTime] <= ? AND [ReturnTime] >= ?) OR ([DepartTime] <= ? AND [ReturnTime] >= ?))""",
                car_id, departTime, departTime, returnTime, returnTime
            )
            return len(cursor.fetchall()) > 0
        except:
            return False

    @classmethod
    def GetOrigins(cls) -> List[str]:
        cursor = DatabaseManager.query(
            """SELECT [Origin] FROM [TourTBL] GROUP BY [Origin] ORDER BY COUNT([Origin]) DESC"""
        )
        origins = list(map(lambda row: row[0], cursor.fetchall()))
        return origins

    @classmethod
    def GetDestinations(cls) -> List[str]:
        cursor = DatabaseManager.query(
            """SELECT [Destination] FROM [TourTBL] GROUP BY [Destination] ORDER BY COUNT([Destination]) DESC"""
        )
        destinations = list(map(lambda row: row[0], cursor.fetchall()))
        return destinations

    @classmethod
    def SearchTours(cls, destination: str = None, origin: str = None, capacity: int = None, fromTime: datetime = None, toTime: datetime = None, status: str = None, includePassengers: bool = False, includeCars: bool = False) -> List[Row]:
        queryString = "SELECT t.[Id], t.[Destination], t.[Origin], t.[Capacity], t.[DepartTime], t.[ReturnTime], t.[Status] "
        if includePassengers:
            queryString += ', group_concat(p.[PassengerId], "-") AS Passengers '
        if includeCars:
            queryString += ', group_concat(c.[CarId], "-") AS Cars '

        queryString += "FROM [TourTBL] AS t "
        conditions = list()
        params = list()
        if includePassengers:
            queryString += "LEFT JOIN [TourPassengersTBL] AS p ON t.Id = p.TourId "
        if includeCars:
            queryString += "LEFT JOIN [TourCarsTBL] AS c ON t.Id = c.TourId "
        if destination is not None:
            conditions.append(f'[Destination] LIKE ?')
            params.append(f'%{destination}%')
        if origin is not None:
            conditions.append(f'[Origin] LIKE ?')
            params.append(f'%{origin}%')
        if capacity is not None:
            conditions.append(f"[Capacity] = ?")
            params.append(capacity)
        if fromTime is not None:
            conditions.append(f"([DepartTime] >= ? OR [ReturnTime] >= ?)")
            params.append(fromTime)
            params.append(fromTime)
        if toTime is not None:
            conditions.append(f"([DepartTime] <= ? OR [ReturnTime] <= ?)")
            params.append(toTime)
            params.append(toTime)
        if status is not None:
            conditions.append(f"[Status] = ?")
            params.append(status)
        if len(conditions) > 0:
            queryString += "WHERE " + ' AND '.join(conditions)
        if includePassengers or includeCars:
            queryString += " GROUP BY t.[Id]"
        cursor = DatabaseManager.query(queryString, *params)
        return cursor.fetchall()

    @classmethod
    def ConfirmTour(cls, Id: int) -> bool:
        try:
            cursor = DatabaseManager.execute(
                f"UPDATE [TourTBL] SET [Status] = ? WHERE [Id] = ?",
                TourStatus.Registering, Id
            )
            return cursor.rowcount == 1
        except Exception as e:
            print(e)
            return False
