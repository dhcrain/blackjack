from my_deck import Deck


class Hand:

    def __init__(self):
        self.cards = []
        self.total = 0
        self.game_deck = Deck().deck

    def hand_value(self):
        return sum(self.cards)

    def deal_cards(self):
        self.cards = [self.game_deck.pop() for _ in range(2)]
        print(self.cards)

hand = Hand()
hand.deal_cards()

