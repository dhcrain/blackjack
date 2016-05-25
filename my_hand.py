import my_deck
import my_cards


class Hand:

    def __init__(self):
        self.count = 0
        self.cards = []
        self.total = 0

    def hand_value(self):
        return sum(self.cards)
