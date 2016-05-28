from my_deck import Deck
import os

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
                self.hand_total += 11  # OR 1, somehow...
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
        else:
            print("Else: win_bust")

    def deal_cards(self):
        self.hand = [self.game_deck.pop() for _ in range(2)]
        # print(self.hand)

    def draw(self):
        self.hand.append(self.game_deck.pop())

    def show_cards(self):
        # card visibility?
        pass

# test_player = Player()
# test_player.deal_cards()
# test_player.draw()
# test_player.hand_value()


class Dealer(Player):

    def dealer_draw(self):
        print("Dealer: ")
        # print(self.hand)
        # print(super().hand_value())
        while super().hand_value() <= 17:
            super().draw()
            print(self.hand)
        print(super().hand_value())
        super().win_bust()
        return super().hand_value()

# dealer = Dealer()
# dealer.deal_cards()


class User(Player):

    def user_draw(self):
        # os.system("clear")
        print("User: ")
        print(self.hand)
        print(super().hand_value())
        while super().hand_value() < 21:
            if input("Draw? Y/n ").lower() != "n":
                super().draw()
            else:
                break
            print(self.hand)
            print(super().hand_value())
        super().win_bust()
        return super().hand_value()


# test_user = User()
# test_user.deal_cards()
# test_user.user_draw()
# test_user.win_bust()

# dealer.dealer_draw()

# dealer.win_bust()
