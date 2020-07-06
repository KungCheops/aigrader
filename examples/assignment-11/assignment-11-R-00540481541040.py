import random
SUITS = ['d', 'c', 'h', 's']
ACE = 0


class Card:
    """ Helper class to represent card structure"""

    def __init__(self, suit, number):
        self.suit = suit
        self.number = number


def createDeck():
    deck = []
    for number in range(0, 13):
        deck.extend([Card(suit, number) for suit in SUITS])
    return deck


def randomHand(deck, k):
    if k > len(deck):
        raise Exception('Not enough cards in deck')
    hand = []
    for i in range(k):
        random_index = int(random.random() * len(deck))
        hand.append(deck.pop(random_index))
    return hand


def do_test(k, n, count_hand):
    """ 
        Structure of tests with random hands
        k - size of hands from deck
        n - number of times to run the test
        count_hand - function to count values for the test
    """
    agg = 0
    for i in range(n):
        deck = createDeck()
        agg += count_hand(randomHand(deck, k))
    return agg / n


def averageAces(k, n):
    count_aces_in_hand = lambda hand: len([c for c in hand if c.number == ACE])
    return do_test(k, n, count_aces_in_hand)


def averageSuits(k, n):
    count_suits_in_hand = lambda hand: len({c.suit for c in hand})
    return do_test(k, n, count_suits_in_hand)


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
    assert 3 <= averageSuits(5, 100) <= 4
    assert 3.99 < averageSuits(52, 10000) <= 4
    assert 3.99 < averageAces(52, 10000) <= 4
