from Models.DatabaseManager import DatabaseManager


class CarType:
    Bus = 'اتوبوس'
    Minibus = 'ميني بوس'
    Van = 'ون'


class Car:
    class CarTag:
        def __init__(self, tag: str):
            import re
            pattern = r'^(\d{2})([بجچدذرزسشصطعفقکلمنوهي])(\d{3})-(\d{2})$'
            match = re.match(pattern, tag)
            if match:
                self.firstPart = match.group(1)
                self.letter = match.group(2)
                self.secondPart = match.group(3)
                self.cityCode = match.group(4)
            else:
                self.firstPart = ''
                self.letter = ''
                self.secondPart = ''
                self.cityCode = ''

        def __repr__(self):
            if self.firstPart and self.letter and self.secondPart and self.cityCode:
                return f'{self.firstPart}{self.letter}{self.secondPart}-{self.cityCode}'
            else:
                return 'پلاک نامعتبر'

    def __init__(self, Id: int, car_type: str, capacity: int, tag: str, driverName: str, driverId: str, driverPhone: str = None):
        self.id = Id
        self.type = car_type
        self.capacity = capacity
        self.tag = Car.CarTag(tag)
        self.driverName = driverName
        self.driverId = driverId
        self.driverPhone = driverPhone

    @classmethod
    def CheckTagExists(cls, tag: str) -> bool:
        cursor = DatabaseManager.execute("""SELECT COUNT(*) FROM [CarTBL] WHERE [CarTag] = ?""", tag)
        count = cursor.fetchone()["COUNT"]
        return count != 0

    @classmethod
    def CreateCar(cls, car_type: str, capacity: int, tag: str, driver_name: str, driver_id: str, driver_phone: str = None) -> bool:
        try:
            cursor = DatabaseManager.execute(
                """INSERT INTO [CarTBL]
                ([Type], [Capacity], [CarTag], [DriverName], [DriverID], [DriverPhone])
                VALUES 
                (?, ?, ?, ?, ?, ?)""",
                car_type, capacity, tag, driver_name, driver_id, driver_phone
            )
            return cursor.rowcount == 1
        except:
            return False

    @classmethod
    def ModifyCar(cls, Id: int, car_type: str, capacity: int, tag: str, driver_name: str, driver_id: str, driver_phone: str = None) -> bool:
        try:
            cursor = DatabaseManager.execute(
                """UPDATE [CarTBL] SET
                [Type] = ?, [Capacity] = ?, [CarTag] = ?, [DriverName] = ?, [DriverID] = ?, [DriverPhone] = ?
                WHERE
                [Id] = ?""",
                car_type, capacity, tag, driver_name, driver_id, driver_phone, Id
            )
            return cursor.rowcount == 1
        except:
            return False

    @classmethod
    def DeleteCar(cls, Id: int) -> bool:
        try:
            cursor = DatabaseManager.execute("""DELETE FROM [CarTBL] WHERE [Id] = ?""", Id)
            return cursor.rowcount == 1
        except:
            return False
