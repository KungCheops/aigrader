import random
import math


def createDeck():
    result = []
    for i in range(1, 53):
        result.append(random.randrange(1, 53))
    return result


def randomHand(deck, k):
    deck = createDeck()
    hand = []
    random.shuffle(deck)
    for k in deck:
        hand.append(deck[k])
    return hand


def averageAces(k, n):
    deck = createDeck()
    for i in range(n):
        aces_prop = 4 / 52
    average = aces_prop * k
    return average


def averageSuits(k, n):
    deck = createDeck()
    suits_prop = 13 / 52
    for i in range(n):
        average = suits_prop * k
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
