import random


class Deck:

    def __init__(self):
        self.card_numbers = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.card_suit = ["♥", "♦", "♠", "♣"]
        self.deck = [(num + " " + suit) for num in self.card_numbers for suit in self.card_suit]
        random.shuffle(self.deck)
        # print(self.deck)


game_deck = Deck()

while True:
    # get cards from deck to hand - deal?
    hand = [game_deck.deck.pop() for _ in range(2)]
    print(hand)

    hand_value = 0
    for card in hand:
        if card[0] in "JQK":
            hand_value += 10
        elif card[0] is "A":
            hand_value += 11    # OR 1, somehow...
        else:
            hand_value += int(card[0])
        print(hand_value)

    print("Hand Value " + str(hand_value))

    # get another card
    while hand_value < 21:
        print("Hand Value " + str(hand_value))
        if input("Draw? Y/n ").lower() != "n":
            hand.append(game_deck.deck.pop())
        else:
            break
        # print(hand)



