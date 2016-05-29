from my_player import Dealer
from my_player import User
import os
import time


class Game:

    def __init__(self):
        self.dealer_hand_value = Dealer().hand_value()
        self.user_hand_value = User().hand_value()

    def play_blackjack(self):
        os.system("clear")
        print("\n      -*-*- Blackjack -*-*-   \n\n"
              "Closest to 21 without going over\n"
              "Dealer stands on 17\n"
              "----------------------------")
        print("Dealer: ", end="")
        dealer.deal_cards()
        print(" ".join(dealer.hand))
        print("\nYour Cards ", end="")
        user.deal_cards()
        print(" ".join(user.hand))
        user.user_draw()
        user.hand_value()
        dealer.dealer_draw()
        print("\nDealer has {}, and you have {}.\n".format(dealer.hand_value(), user.hand_value()))
        game.winner()

    def winner(self):
        self.you_win = " *** You Win! ***\n"
        self.dealer_win = " * Dealer Wins! *\n"
        if user.bust and dealer.bust:
            print("Both busted, Dealer wins")
        elif dealer.hand_value() > user.hand_value():
            if dealer.bust and not user.bust:
                print(self.you_win)
                game.play_again()
            print(self.dealer_win)
            game.play_again()
        elif dealer.hand_value() < user.hand_value():
            if user.bust:
                print(self.dealer_win)
                game.play_again()
            print(self.you_win)
        elif dealer.hand_value() == user.hand_value():
            if dealer.win and user.win:
                print(" * Both have Blackjack, Dealer Wins! *")
            else:
                print("Push, tie, keep your money.")
        elif dealer.win and not user.win:
            print(" * Dealer Wins! *")
        else:
            print("That was an odd hand!?!?")
        game.play_again()

    def play_again(self):
        if input("\nPlay Again? Y/n ").lower() != "n":
            print("Shuffling........")
            time.sleep(.5)
            game.play_blackjack()
        else:
            print("\nThanks for playing Blackjack")
            exit()

game = Game()
dealer = Dealer()
user = User()
game.play_blackjack()
