from my_deck import Deck


class Player:

    def __init__(self):
        self.hand = []
        self.hand_total = 0
        self.game_deck = Deck().deck

    def hand_value(self):
        print(self.hand)
        self.hand_total = 0
        for card in self.hand:
            if card[0] in "1JQK":
                self.hand_total += 10
            elif card[0] is "A":
                self.hand_total += 11  # OR 1, somehow...
            else:
                self.hand_total += int(card[0])
            return self.hand_total
            # print(self.hand_total)
        print("Hand Value " + self.hand_value)

        # go to calc the value of cards somehow.....
        # return sum(self.cards) ?
        pass

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
        pass
        # if hand_total <= 17:
        #     super().draw()
        # elif hand_total > 21:
        #     print(Dealer Lost)
        # else:
        #     print(Dealer Wins)


class User(Player):

    def user_draw(self):
        print(self.hand)
        print(super().hand_value())
        if input("Draw? Y/n ").lower() != "n":
            super().draw()
        else:
            pass
        print(self.hand)


# test_user = User()
# test_user.deal_cards()
# test_user.user_draw()
