

class Boxer:

    def __init__(self, name, wins, losses, weight):
        self.name=name
        self.wins=wins
        self.losses=losses
        self.weight = weight

    def __str__(self):
        return self.name + " is " + str(self.wins) + "-" + str(self.losses)

    def fight(self, otherGuy):

        if self.weight > otherGuy.weight:
            self.wins += 1
            otherGuy.losses += 1

        else:
            self.losses += 1
            otherGuy.wins += 1

che = Boxer("Che", 0, 0, 100)
jackson = Boxer("Jackson", 0, 0, 105)
zenas = Boxer("Zenas", 0, 0, 120)

che.fight(zenas)
zenas.fight(jackson)
jackson.fight(che)

print(che)
print(jackson)
print(zenas)