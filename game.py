from my_player import Player
from my_player import Dealer
from my_player import User


class Game:

    def __init__(self):
        self.dealer_hand_value = Dealer().hand_value()
        self.user_hand_value = User().hand_value()
        self.blackjack = False

    def winner(self):
        if self.dealer_hand_value > self.user_hand_value:
            print("Dealer Wins!")
            exit()  # play again
        elif self.dealer_hand_value < self.user_hand_value:
            print("You Win!")
            exit()
        elif self.dealer_hand_value == 21 and self.user_hand_value == 21:
            print("Tie, Dealer Wins!")
            exit()
        else:
            print("ELSE Both busted, sad")
            exit()
"""
    def win_bust(self):
        if Player().hand_value() > 21:
            print("\n ** Bust! ** ")
        elif Player().hand_value() == 21:
            print("\n *** BlackJack! *** ")
            self.blackjack = True
        else:
            pass
"""


dealer = Dealer()
user = User()
game = Game()

user.deal_cards()
user.user_draw()
user.hand_value()
# game.winner()

dealer.dealer_draw()
dealer.hand_value()

game.winner()
