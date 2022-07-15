from DatabaseGenerator.TestPassenger import *
from DatabaseGenerator.TestCar import *
from DatabaseGenerator.TestTour import *
from random import sample
from datetime import timedelta

psg_file = open('Passengers.txt', 'r')
psg_file.readline()  # Skip titles
passengers = list()
for line in psg_file:
    if line[-1] == '\n':
        line = line[:-1]
    l = line.split(',')
    try:
        passengers.append(TestPassenger(l[0], l[1], l[2], l[3], l[4]))
    except:
        pass

psg_file.close()

car_file = open('Cars.txt', 'r')
car_file.readline()  # skip titles
cars = list()
car_id = 1
for line in car_file:
    if line[-1] == '\n':
        line = line[:-1]
    l = line.split(',')
    try:
        cars.append(Car(car_id, l[0], int(l[1]), l[2], l[3], l[4], l[5]))
        car_id += 1
    except:
        pass

car_file.close()

tour_file = open('Tours.txt', 'r')
tour_file.readline()  # skip titles
tours = list()
tour_id = 1
for line in tour_file:
    l = line.split(',')
    try:
        tours.append(TestTour(tour_id, l[0], l[1], int(l[2]), l[3], l[4], l[5], passengers=[], cars=[*l[6:]]))
        tours[tour_id - 1].departTime += timedelta(seconds=1)
        tours[tour_id - 1].returnTime += timedelta(seconds=1)
        tours[tour_id - 1].passengers = list(map(lambda p: p.id, sample(passengers, tours[tour_id - 1].capacity)))

        tour_id += 1
    except:
        pass

# Generating SQL command to insert passengers
psg_sql = open('passengers.sql', 'w')
psg_sql.write('INSERT INTO [PassengerTBL]\n')
psg_sql.write('COLUMNS ([Id], [Name], [Family], [FatherName], [Phone])\n')
psg_sql.write('VALUES\n')

cmd = list()
for p in passengers:
    cmd.append(f"('{p.id}', N'{p.name}', N'{p.family}', N'{p.father}', N'{p.phone}'),\n")
psg_sql.writelines(cmd)
psg_sql.close()

# Generating SQL command to insert cars
car_sql = open('cars.sql', 'w')
car_sql.write('INSERT INTO [CarTBL]\n')
car_sql.write('([Type], [Capacity], [CarTag], [DriverName], [DriverID], [DriverPhone])\n')
car_sql.write('VALUES\n')

cmd = list()
for c in cars:
    phone = f"N'{c.driverPhone}'" if c.driverPhone else 'NULL'
    cmd.append(f"(N'{c.type}', {c.capacity}, N'{str(c.tag)}', N'{c.driverName}', N'{c.driverId}', {phone}),\n")
car_sql.writelines(cmd)
car_sql.close()

# Generating SQL command to insert tours
tour_sql = open('tours.sql', 'w')
tour_sql.write('INSERT INTO [TourTBL]\n')
tour_sql.write('([Destination], [Origin], [Capacity], [DepartTime], [ReturnTime], [Status], [Passengers], [Cars])\n')
tour_sql.write('VALUES\n')

cmd = list()
for t in tours:
    psg = "'" + '-'.join(t.passengers) + "'" if t.passengers else 'NULL'
    cr = "'" + '-'.join(t.cars) + "'" if t.cars else 'NULL'
    cmd.append(
        f"(N'{t.destination}', N'{t.origin}', {t.capacity}, '{t.departTime.strftime('%Y-%m-%d %H:%M')}', '{t.returnTime.strftime('%Y-%m-%d %H:%M')}', N'{t.status}' {psg}, {cr}),\n")
tour_sql.writelines(cmd)
tour_sql.close()
