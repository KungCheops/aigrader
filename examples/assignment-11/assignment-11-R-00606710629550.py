import random


class Suit:

    def __init__(self, value):
        self.value = value
        if value == 0:
            self.name = 'Spades'
        elif value == 1:
            self.name = 'Clubs'
        elif value == 2:
            self.name = 'Diamonds'
        elif value == 3:
            self.name = 'Hearts'
        else:
            raise ValueError('value should be between 0 and 3')


class Card:

    def __init__(self, rank, suit):
        if not isinstance(suit, Suit):
            raise ValueError('suit must be of type Suit')
        self.rank = rank
        self.suit = suit
        if rank == 1:
            self.name = '{0} of {1}'.format('Ace', self.suit.name)
        elif rank == 11:
            self.name = '{0} of {1}'.format('Jack', self.suit.name)
        elif rank == 12:
            self.name = '{0} of {1}'.format('Queen', self.suit.name)
        elif rank == 13:
            self.name = '{0} of {1}'.format('King', self.suit.name)
        else:
            self.name = '{0} of {1}'.format(self.rank, self.suit.name)


class Deck:

    def __init__(self):
        self.cards = []
        self.graveyard = []
        self.build()

    def build(self):
        for i in range(0, 52):
            suit = Suit(i % 4)
            card = Card(i % 13 + 1, suit)
            self.cards.append(card)

    def mix_with_graveyard(self):
        for card in self.graveyard:
            self.cards.append(card)
        del self.graveyard[:]

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        card = self.cards.pop()
        self.graveyard.append(card)
        return card

    def show(self):
        for card in self.cards:
            print(card.name)

    def show_graveyard(self):
        for card in self.graveyard:
            print(card.name)


def createDeck():
    result = Deck()
    return result


def randomHand(deck, k):
    if k > len(deck.cards):
        raise ValueError('cannot draw {0} cards from a deck of {1} cards'.
            format(k, len(deck.cards)))
    hand = []
    deck.shuffle()
    for _ in range(k):
        hand.append(deck.draw_card())
    return hand


"""
Calculates the average of something in a deck. The summer is a function
that takes a hand and returns the number of observations in that hand that
fulfills a certain criteria.
"""


def avgFunc(k, n, summer):
    if n == 0:
        return 0
    deck = createDeck()
    obs_sum = 0
    for _ in range(n):
        deck.mix_with_graveyard()
        hand = randomHand(deck, k)
        obs_sum += summer(hand)
    return obs_sum / n


def averageAces(k, n):

    def num_aces_in_hand(hand):
        num_aces = 0
        for card in hand:
            if card.rank == 13:
                num_aces += 1
        return num_aces
    average = avgFunc(k, n, num_aces_in_hand)
    return average


def averageSuits(k, n):

    def num_distinct_suits_in_hand(hand):
        distinct_suits = set()
        for card in hand:
            distinct_suits.add(card.suit.value)
        return len(distinct_suits)
    average = avgFunc(k, n, num_distinct_suits_in_hand)
    return average


def run(k, n):
    print(
        f'Average number of aces in hands of size {k} in {n} trials is {averageAces(k, n)}'
        )
    print(
        f'Average number of distinct suits in hands of size {k} in {n} trials is {averageSuits(k, n)}'
        )


if __name__ == '__main__':
    run(5, 100)
    assert 0.2 < averageAces(5, 100) < 0.6
