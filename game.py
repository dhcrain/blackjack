from my_player import Player
from my_player import Dealer
from my_player import User


class Game:

    def __init__(self):
        self.dealer_hand_value = Dealer().hand_value()
        self.user_hand_value = User().hand_value()
        self.blackjack = False

    def winner(self):
        if dealer.hand_value() > user.hand_value():
            if dealer.bust:
                print("1You Win!")
                exit()
            print("2Dealer Wins!")
            exit()  # play again
        elif dealer.hand_value() < user.hand_value():
            if user.bust:
                print("3Dealer Wins!")
                exit()
            print("4You Win!")
            exit()
        elif dealer.hand_value() == 21 and user.hand_value() == 21:
            print("5Tie, Dealer Wins!")
            exit()
        else:
            print("6ELSE Both busted, sad")
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
# dealer.hand_value()

game.winner()
