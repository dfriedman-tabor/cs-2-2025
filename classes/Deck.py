from random import randint

class Card:
    def __init__(self, suit, num):
        self.suit = suit
        self.num = num

    def __str__(self):
        return str(self.num) + " of " + self.suit

class Deck:

    def __init__(self):
        self.cards = []

        for i in range(1, 14):
            for suit in ["spades", "diamonds", "hearts", "clubs"]:
                self.cards.append(Card(suit, i))

    def __str__(self):
        output = ""
        for card in self.cards:
            output += str(card)
            output += "\n"

        return output



myDeck = Deck()

print(myDeck)



