from Animal import *

class Zoo:

    def __init__(self, animals):
        self.animals = animals

    def __str__(self):
        output = "Here are the animals in this zoo:"
        for animal in self.animals:
            output += "\n" + str(animal)
        return output

    def raucous(self):
        for animal in self.animals:
            animal.speak()

    def averageDanger(self):
        avg = 0
        for animal in self.animals:
            avg += animal.dangerLevel
        print(avg/len(self.animals))


myZoo = Zoo([Animal("lion", "roar", 9), Animal("tiger", "grrr", 8), Animal("llama", "spit", 5), Animal("termite", "chitter", 1) ])

print(myZoo)