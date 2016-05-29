from my_deck import Deck
import time


class Player:

    def __init__(self):
        self.hand = []
        self.hand_total = 0
        self.game_deck = Deck().deck
        self.win = False
        self.bust = False

    def hand_value(self):
        self.hand_total = 0
        for card in self.hand:
            if card[0] in "1JQK":
                self.hand_total += 10
            elif card[0] is "A":
                if self.hand_total + 11 <= 21:
                    self.hand_total += 11
                elif self.hand_total > 21:
                    self.hand_total += 1
            else:
                self.hand_total += int(card[0])
        return int(self.hand_total)

    def win_bust(self):
        if self.hand_value() > 21:
            print("\n ** Bust! ** \n")
            self.bust = True
        elif self.hand_value() == 21:
            print("\n *** Blackjack! *** \n")
            self.win = True

    def deal_cards(self):
        self.hand = [self.game_deck.pop() for _ in range(2)]

    def draw(self):
        self.hand.append(self.game_deck.pop())


class Dealer(Player):

    def dealer_draw(self):
        while super().hand_value() <= 17:
            super().draw()
            time.sleep(.1)
            print("Dealer Draws: ", " ".join(self.hand))
        super().win_bust()
        return super().hand_value()


class User(Player):

    def user_draw(self):
        while super().hand_value() < 21:
            if input("Hit or Stand? H/s ").lower() != "s":
                print("Your new cards: ", end="")
                super().draw()
            else:
                print(" ")
                break
            print(" ".join(self.hand))
        super().win_bust()
        return super().hand_value()
