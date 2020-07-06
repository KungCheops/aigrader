import random
from collections import Counter
from random import shuffle


def createDeck():
    faces = []
    suits = ['Spade', 'Heart', 'Diamond', 'Club']
    royals = ['J', 'Q', 'K', 'A']
    result = []
    for i in range(2, 11):
        faces.append(str(i))
    for j in range(4):
        faces.append(royals[j])
    for k in range(4):
        for l in range(13):
            card = [suits[k], faces[l]]
            result.append(card)
    return result


def randomHand(deck, k):
    shuffle(deck)
    hand = random.sample(deck, k=k)
    return hand


def averageAces(k, n):
    deck = createDeck()
    aces = []
    for i in range(0, n):
        hands = randomHand(deck, k)
        c = sum(x.count('A') for x in hands)
        aces.append(c)
    average = sum(aces) / n
    return average


def averageSuits(k, n):
    deck = createDeck()
    count = []
    c = []
    for i in range(0, n):
        hands = randomHand(deck, k)
        H = sum(x.count('Heart') for x in hands)
        D = sum(x.count('Diamond') for x in hands)
        S = sum(x.count('Spade') for x in hands)
        C = sum(x.count('Club') for x in hands)
        count.append(H)
        count.append(D)
        count.append(S)
        count.append(C)
    for j in count:
        if j == 1:
            c.append(j)
        elif j == 2:
            c.append(j - 1)
        elif j == 3:
            c.append(j - 2)
        elif j == 4:
            c.append(j - 3)
    average = sum(c) / n
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
