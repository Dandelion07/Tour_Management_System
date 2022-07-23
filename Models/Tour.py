from typing import List, Optional
import jdatetime
from Models.DatabaseManager import DatabaseManager
from datetime import datetime
from Models.Passenger import Passenger


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
    def SearchTours(cls, destination: str = None, origin: str = None, capacity: int = None, fromTime: datetime = None, toTime: datetime = None, status: str = None, includePassengers: bool = False, includeCars: bool = False) -> List['Tour']:
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
        rows = cursor.fetchall()
        tours = list()
        for row in rows:
            tours.append(Tour(
                row["Id"],
                row["Destination"],
                row["Origin"],
                row["Capacity"],
                jdatetime.datetime.fromgregorian(datetime=datetime.fromisoformat(row["DepartTime"])),
                jdatetime.datetime.fromgregorian(datetime=datetime.fromisoformat(row["ReturnTime"])),
                row["Status"],
                row["Passengers"].split("-") if row["Passengers"] is not None else list(),
                row["Cars"].split("-") if row["Cars"] is not None else list()
            ))
        return tours

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

    @classmethod
    def SearchTourById(cls, Id: int) -> Optional['Tour']:
        cursor = DatabaseManager.query(
            """
            SELECT t.[Id], t.[Destination], t.[Origin], t.[Capacity], t.[DepartTime], t.[ReturnTime], t.[Status]
            , group_concat(p.[PassengerId], '-') AS Passengers 
            , group_concat(c.[CarId], '-') AS Cars 
            FROM [TourTBL] AS t 
            LEFT JOIN [TourPassengersTBL] AS p ON t.Id = p.TourId 
            LEFT JOIN [TourCarsTBL] AS c ON t.Id = c.TourId 
            WHERE t.[Id] = ?
            GROUP BY t.[Id]
            """, Id
        )
        row = cursor.fetchone()
        if not row:
            return None
        return Tour(
            row["Id"],
            row["Destination"],
            row["Origin"],
            row["Capacity"],
            jdatetime.datetime.fromgregorian(datetime=datetime.fromisoformat(row["DepartTime"])),
            jdatetime.datetime.fromgregorian(datetime=datetime.fromisoformat(row["ReturnTime"])),
            row["Status"],
            row["Passengers"].split("-") if row["Passengers"] is not None else list(),
            row["Cars"].split("-") if row["Cars"] is not None else list()
        )

    @classmethod
    def RegisterPassenger(cls, tour: 'Tour', passengerId: str) -> bool:
        if len(tour.passengers) >= tour.capacity:
            return False
        if passengerId in tour.passengers:
            return False
        tour.passengers.append(passengerId)

        cursor = DatabaseManager.execute(
            """
            INSERT INTO [TourPassengersTBL] (TourId, PassengerId) 
            VALUES (?, ?)
            """,
            tour.id, passengerId
        )
        if cursor.rowcount != 1:
            return False

        if len(tour.passengers) == tour.capacity:
            tour.status = TourStatus.FullCapacity
            cursor = DatabaseManager.execute(
                """
                UPDATE [TourTBL] SET
                [Status] = ?
                WHERE [Id] = ?
                """,
                tour.status, tour.id
            )
            return cursor.rowcount == 1
        return True

    @classmethod
    def SearchTourPassengers(cls, tourId: int, passengerId: str = None, name: str = None, family: str = None, father: str = None, phone: str = None) -> List[Passenger]:
        query_string = """
                        SELECT t.TourId, p.Id, p.Name, p.Family, p.FatherName, p.Phone FROM [TourPassengersTBL] AS t
                        INNER JOIN [PassengerTBL] AS p on t.[PassengerId] = p.[Id]
                        """
        conditions = list()
        params = list()

        conditions.append('t.TourId = ?')
        params.append(tourId)

        if passengerId is not None:
            conditions.append('p.Id = ?')
            params.append(passengerId)

        if name is not None:
            conditions.append('p.Name LIKE ?')
            params.append(f'%{name}%')

        if family is not None:
            conditions.append('p.Family LIKE ?')
            params.append(f'%{family}%')

        if father is not None:
            conditions.append('p.FatherName LIKE ?')
            params.append(f'%{father}%')

        if phone is not None:
            conditions.append('p.Phone LIKE ?')
            params.append(f'%{phone}%')

        query_string += ' WHERE ' + ' AND '.join(conditions)
        cursor = DatabaseManager.query(query_string, *params)
        rows = cursor.fetchall()
        passengers = list()
        for row in rows:
            passengers.append(Passenger(
                row["Id"],
                row["Name"],
                row["Family"],
                row["FatherName"],
                row["Phone"]
            ))
        return passengers

    @classmethod
    def CancelRegistration(cls, tourId: int, passengerId: List[str]) -> bool:
        cursor = DatabaseManager.execute(
            f"DELETE FROM TourPassengersTBL WHERE TourId = ? AND PassengerId IN ({','.join('?' for _ in range(len(passengerId)))})",
            tourId, *passengerId
        )
        if cursor.rowcount != len(passengerId):
            return False

        cursor = DatabaseManager.execute(
            """
            UPDATE [TourTBL] SET [Status] = ? WHERE [Id] = ?
            """,
            TourStatus.Registering, tourId
        )
        return cursor.rowcount == 1
