from typing import List, Tuple

from pyodbc import Row

from Models.DatabaseManager import DatabaseManager
from datetime import datetime


class TourStatus:
    NotConfirmed = 'تاييد نشده'
    Registering = 'در حال ثبت نام'
    FullCapacity = 'تکميل ظرفيت'
    Ended = 'برگزار شده'
    Canceled = 'حذف شده'


class Tour:
    def __init__(self, id: int, destination: str, origin: str, capacity: int, departTime: str, returnTime: str,
                 status: str, passengers: list = None, cars: list = None):
        self.id = id
        self.destination = destination
        self.origin = origin
        self.capacity = capacity if capacity > 0 else 0
        self.departTime = datetime.fromisoformat(departTime)
        self.returnTime = datetime.fromisoformat(returnTime)
        self.status = status
        self.passengers = list()

        for p in passengers:
            self.passengers.append(p)

        self.cars = list()
        for c in cars:
            self.cars.append(c)

    @classmethod
    def CreateTour(cls, destination: str, origin: str, capacity: int, departTime: datetime,
                   returnTime: datetime) -> bool:
        try:
            cursor = DatabaseManager.execute(
                """INSERT INTO [TourTBL]
                ([Destination], [Origin], [Capacity], [DepartTime], [ReturnTime], [Status], [Passengers], [Cars])
                VALUES 
                (?, ?, ?, ?, ?, ?, ?, ?)""",
                destination, origin, capacity, departTime, returnTime, TourStatus.NotConfirmed, '', ''
            )
            return cursor.rowcount == 1
        except:
            return False

    @classmethod
    def DeleteTour(cls, Id: int) -> bool:
        # TODO Change tour status instead of deleting the tour
        try:
            cursor = DatabaseManager.execute(
                """DELETE FROM [TourTBL] WHERE [Id] = ?""", Id
            )
            return cursor.rowcount == 1
        except:
            return False

    @classmethod
    def hasTourInterference(cls, destination: str, origin: str, departTime: datetime, returnTime: datetime) -> bool:
        try:
            cursor = DatabaseManager.query(
                """SELECT COUNT(*) FROM [TourTBL] 
                WHERE [Destination] = ? AND [Origin] = ? AND (([DepartTime] <= ? AND [ReturnTime] >= ?) OR ([DepartTime] <= ? AND [ReturnTime] >= ?))""",
                destination, origin, departTime, departTime, returnTime, returnTime
            )
            return cursor.fetchval() > 0
        except Exception as e:
            print(e)
            return False

    @classmethod
    def hasPassengerInterference(cls, passenger_id: str, departTime: datetime, returnTime: datetime) -> bool:
        try:
            cursor = DatabaseManager.query(
                """SELECT COUNT(value) 
                FROM [TourTBL] 
                CROSS APPLY STRING_SPLIT([Passengers], '-') 
                WHERE value = ? AND (([DepartTime] <= ? AND [ReturnTime] >= ?) OR ([DepartTime] <= ? AND [ReturnTime] >= ?))""",
                passenger_id, departTime, departTime, returnTime, returnTime
            )
            return cursor.fetchval() > 0
        except:
            return False

    @classmethod
    def hasCarInterference(cls, car_id: int, departTime: datetime, returnTime: datetime) -> bool:
        try:
            cursor = DatabaseManager.query(
                """SELECT COUNT(value) 
                FROM [TourTBL] 
                CROSS APPLY STRING_SPLIT([Cars], '-') 
                WHERE value = ? AND (([DepartTime] <= ? AND [ReturnTime] >= ?) OR ([DepartTime] <= ? AND [ReturnTime] >= ?))""",
                car_id, departTime, departTime, returnTime, returnTime
            )
            return cursor.fetchval() > 0
        except:
            return False

    @classmethod
    def GetOrigins(cls) -> List[str]:
        cursor = DatabaseManager.query(
            """SELECT [Origin] FROM [TourTBL] GROUP BY [Origin] ORDER BY COUNT([Origin]) DESC"""
        )
        origins = list(map(lambda row: row.Origin, cursor.fetchall()))
        return origins

    @classmethod
    def GetDestinations(cls) -> List[str]:
        cursor = DatabaseManager.query(
            """SELECT [Destination] FROM [TourTBL] GROUP BY [Destination] ORDER BY COUNT([Destination]) DESC"""
        )
        destinations = list(map(lambda row: row.Destination, cursor.fetchall()))
        return destinations

    @classmethod
    def SearchTours(cls, destination: str = None, origin: str = None, capacity: int = None, fromTime: datetime = None, toTime: datetime = None, status: str = None) -> List[Row]:
        queryString = """SELECT [Id], [Destination], [Origin], [Capacity], [DepartTime], [ReturnTime], [Status], [Passengers], [Cars]  FROM [TourTBL] """
        conditions = list()
        params = list()
        if destination is not None:
            conditions.append(f"[Destination] LIKE N'%?%'")
            params.append(destination)
        if origin is not None:
            conditions.append(f"[Origin] LIKE N'%?%'")
            params.append(origin)
        if capacity is not None:
            conditions.append(f"[Capacity] = ?")
            params.append(capacity)
        if fromTime is not None:
            conditions.append(f"([DepartTime] >= ? OR [ReturnTime) >= ?")
            params.append(fromTime)
            params.append(fromTime)
        if toTime is not None:
            conditions.append(f"([DepartTime] <= ? OR [ReturnTime) <= ?")
            params.append(toTime)
            params.append(toTime)
        if status is not None:
            conditions.append(f"[Status] = ?")
            params.append(status)
        if len(conditions) > 0:
            queryString += "WHERE " + ' AND '.join(conditions)
        cursor = DatabaseManager.query(queryString, *params)
        return cursor.fetchall()
