from Models.DatabaseManager import DatabaseManager


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
            cursor = DatabaseManager.execute("""SELECT [Id] FROM [PassengerTBL] WHERE [Id] = ?""", Id)
            return len(cursor.fetchall()) == 1
        except:
            return False

    @classmethod
    def CreatePassenger(cls, Id: str, name: str, family: str, father: str = None, phone: str = None) -> bool:
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
    def GetPassengerById(cls):
        pass
