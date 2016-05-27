import random


class Deck:

    def __init__(self):
        self.card_numbers = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.card_suit = ["♥", "♦", "♠", "♣"]
        self.deck = [(num + " " + suit) for num in self.card_numbers for suit in self.card_suit]
        random.shuffle(self.deck)
        # print(self.deck)


game_deck = Deck()

hand = [game_deck.deck.pop() for _ in range(2)]


def hand_total():
    hand_value = 0
    for card in hand:
        if card[0] in "1JQK":
            hand_value += 10
        elif card[0] is "A":
            hand_value += 11  # OR 1, somehow...
        else:
            hand_value += int(card[0])
    return hand_value
    
print(hand)
print(hand_total())

while True:
    # hand_value = 0
    # get another card
    while hand_total() < 21:
        if input("Draw? Y/n ").lower() != "n":
            hand.append(game_deck.deck.pop())
        else:
            break
        print(hand_total())
        print(hand)

    # print(hand)
    # print("Hand Value " + str(hand_value))

    if hand_total() > 21:
        print("\n ** Bust! ** ")
        break
    elif hand_total() == 21:
        print("\n *** Winner! *** ")
        break
    else:
        continue


