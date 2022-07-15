import xlrd


class TestTour:
    def __init__(self, id: int, destination: str, origin: str, capacity: int, departTime: str, returnTime: str,
                 status: str, passengers: list = None, cars: list = None):
        self.id = id
        self.destination = destination
        self.origin = origin
        self.capacity = capacity if capacity > 0 else 0
        self.departTime = xlrd.xldate_as_datetime(float(departTime), 0)
        self.returnTime = xlrd.xldate_as_datetime(float(returnTime), 0)
        self.status = status
        self.passengers = list()

        for p in passengers:
            self.passengers.append(p)

        self.cars = list()
        for c in cars:
            self.cars.append(c)
