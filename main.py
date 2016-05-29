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
              "--------------------------------\n")
        dealer.deal_cards()
        print("Dealer's Cards: ", end="")
        print(dealer.hand[0], "| ##")
        print("\nYour Cards:     ", end="")
        user.deal_cards()
        print(" | ".join(user.hand))
        user.user_draw()
        print("Dealers Hand: ", " | ".join(dealer.hand))
        dealer.dealer_draw()
        print("\nDealer has {}, and you have {}.\n".format(dealer.hand_value(), user.hand_value()))
        game.winner()

    def winner(self):
        you_win = " *** You Win! ***\n"
        dealer_win = " * Dealer Wins! *\n"
        if user.hand_value() >= 22 and dealer.hand_value() >= 22:
            print("Both busted, Dealer wins")
        elif dealer.win and not user.win:
            print(dealer_win)
        elif dealer.hand_value() > user.hand_value():
            if dealer.hand_value() >= 22:
                print(you_win)
                game.play_again()
            if user.hand_value() >= 22:
                print(dealer_win)
            print(dealer_win)
            game.play_again()
        elif dealer.hand_value() < user.hand_value():
            if user.hand_value() >= 22:
                print(dealer_win)
                game.play_again()
            print(you_win)
        elif dealer.hand_value() == user.hand_value():
            if dealer.win and user.win:
                print(" * Both have Blackjack, Dealer Wins! *")
            else:
                print("Push, tie, keep your money.")
        else:
            print("Well, that was an odd hand!?!?")
        game.play_again()

    def play_again(self):
        if input("\nPlay Again? Y/n ").lower() != "n":
            for num in range(20):
                print("Shuffling........")
                time.sleep(.02)
            game.play_blackjack()
        else:
            print("\nThanks for playing Blackjack")
            exit()

game = Game()
dealer = Dealer()
user = User()
game.play_blackjack()