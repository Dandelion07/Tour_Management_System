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

    def __init__(self, id: int, type: str, capacity: int, tag: str, driverName: str, driverId: str,
                 driverPhone: str = None):
        self.id = id
        self.type = type
        self.capacity = capacity
        self.tag = Car.CarTag(tag)
        self.driverName = driverName
        self.driverId = driverId
        self.driverPhone = driverPhone

