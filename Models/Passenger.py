import datetime
from typing import Optional, List
import jdatetime
from Models.DatabaseManager import DatabaseManager
from Models import Tour


class Passenger:
    def __init__(self, Id: str, name: str, family: str, father: str = None, phone: str = None) -> None:
        self.id = Id
        self.name = name.strip()
        self.family = family.strip()
        self.father = father
        self.phone = phone if phone is not None and phone.isdigit() else None

    @classmethod
    def CheckExists(cls, Id: str) -> bool:
        try:
            cursor = DatabaseManager.query("""SELECT [Id] FROM [PassengerTBL] WHERE [Id] = ?""", Id)
            return len(cursor.fetchall()) == 1
        except:
            return False

    @classmethod
    def CreatePassenger(cls, Id: str, name: str, family: str, father: str = None, phone: str = None) -> bool:
        if cls.CheckExists(Id):
            return False
        try:
            cursor = DatabaseManager.execute(
                """INSERT INTO [PassengerTBL]
                ([Id], [Name], [Family], [FatherName], [Phone])
                VALUES
                (?, ?, ?, ?, ?)""",
                Id, name, family, father, phone
            )
            return cursor.rowcount == 1
        except:
            return False

    @classmethod
    def ModifyPassenger(cls, Id: str, name: str, family: str, father: str = None, phone: str = None) -> bool:
        try:
            cursor = DatabaseManager.execute(
                """UPDATE [PassengerTBL] SET
                [Name] = ?, [Family] = ?, [FatherName] = ?, [Phone] = ?
                WHERE [Id] = ?""",
                name, family, father, phone, Id
            )
            return cursor.rowcount == 1
        except:
            return False

    @classmethod
    def DeletePassenger(cls, Id: str) -> bool:
        try:
            cursor = DatabaseManager.execute(
                """DELETE FROM [PassengerTBL]
                WHERE [Id] = ?""",
                Id
            )
            return cursor.rowcount == 1
        except:
            return False

    @classmethod
    def GetPassengerById(cls, Id: str) -> Optional['Passenger']:
        cursor = DatabaseManager.query(
            """SELECT [Id], [Name], [Family], [FatherName], [Phone] FROM [PassengerTBL]
            WHERE [Id] = ?""", Id)
        p = cursor.fetchall()
        if len(p) != 1:
            return None
        p = p[0]
        return Passenger(p["Id"], p["Name"], p["Family"], p["FatherName"], p["Phone"])

    @classmethod
    def SearchPassengerHistory(cls, Id: str) -> Optional[List['Tour']]:
        cursor = DatabaseManager.query(
            """
            SELECT t.Id, t.Origin, t.Destination, t.Capacity, t.DepartTime, t.ReturnTime, t.Status FROM [TourPassengersTBL] AS tp
            INNER JOIN TourTBL AS t ON tp.TourId = t.Id
            WHERE tp.PassengerId = ?
            """,
            Id
        )
        rows = cursor.fetchall()
        tours = list()
        for row in rows:
            tour = Tour.Tour(
                int(row["Id"]),
                row["Destination"],
                row["Origin"],
                int(row["Capacity"]),
                jdatetime.datetime.fromgregorian(datetime=datetime.datetime.fromisoformat(row["DepartTime"])),
                jdatetime.datetime.fromgregorian(datetime=datetime.datetime.fromisoformat(row["ReturnTime"])),
                row["Status"]
            )
            tour.passengers = Tour.Tour.SearchTourPassengers(tour.id)
            tours.append(tour)
        return tours
