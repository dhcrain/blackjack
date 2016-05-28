


class Card:

    def __init__(self):
        self.value = 4
        self.suit = "Spade"
        self.visible = True

    def __str__(self):
        return "{} {}".format(self.value, self.suit)

    def __repr__(self):
        return "{} {}".format(self.value, self.suit)

hand = [Card(), Card()]
print(hand)
