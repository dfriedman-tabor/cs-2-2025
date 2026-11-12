from Car import *

class Garage:

    def __init__(self, size):
        self.slots = []
        for i in range(size):
            self.slots.append(None)

    def addCar(self, car, i):
        self.slots[i] = car

    def totalWorth(self):
        total = 0
        for car in self.slots:
            if car != None:
                total += car.worth()
        print(total)


    def drive(self, i, distance):
        if self.slots[i] != None:
            self.slots[i].drive(distance)
        else:
            print("there is no car there")


myGarage = Garage(5)

myGarage.addCar(Car("Honda", "Civic", 2020, 60000, 30000), 0)
myGarage.addCar(Car("Honda", "Civic", 2020, 60000, 30000), 3)

myGarage.totalWorth()
myGarage.drive(3, 300)