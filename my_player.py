from my_deck import Deck


class Player:

    def __init__(self):
        self.hand = []
        self.hand_total = 0
        self.game_deck = Deck().deck

    def hand_value(self):
        for card in self.hand:
            sum(int(card[0]))

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


class Dealer(Player):

    def dealer_draw(self):
        pass
        # if hand_total <= 17:
        #     self.hand.append(self.game_deck.pop())
        # elif hand_total > 21:
        #     print(Dealer Lost)
        # else:
        #     print(Dealer Wins)


class User(Player):

    def user_draw(self):
        print(self.hand)
        if input("Draw? Y/n ").lower() != "n":
            super().draw()
        else:
            pass
        print(self.hand)


test_user = User()
test_user.deal_cards()
test_user.user_draw()
