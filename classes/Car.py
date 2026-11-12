class Car:
    def __init__(self, make, model, year, mileage, value):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.value = value

    def __str__(self):
        return self.make + " " + self.model

    def drive(self, distance):
        self.mileage += distance

    def worth(self):
        age = 2026 - self.year
        value = self.value - (age * 1000 + self.mileage / 10)

        return max(value, 2000)


myCar = Car("Honda", "Civic", 2020, 60000, 30000)

print(myCar.worth())

myCar.drive(1000)