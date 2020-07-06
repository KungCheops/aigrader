import random


def createDeck():
    result = []
    for suit in ('h', 's', 'd', 'c'):
        for rank in range(1, 14):
            result.append([suit, rank])
    random.shuffle(result)
    return result


def randomHand(deck, k):
    if not (k <= 52 and k >= 1) or type(k) != int:
        raise ValueError('k should be an integer between 1 and 52')
    hand = [None] * k
    for i in range(0, k):
        hand[i] = deck[random.randint(0, 51)]
    return hand


def averageAces(k, n):
    deck = createDeck()
    if not (k <= 52 and k >= 1) or type(k) != int:
        raise ValueError('k should be an integer between 1 and 52')
    aces = 0
    for i in range(0, n):
        hand = randomHand(deck, k)
        for card in hand:
            if card[1] == 1:
                aces += 1
    average = aces / n
    return average


def averageSuits(k, n):
    deck = createDeck()
    if not (k <= 52 and k >= 1) or type(k) != int:
        raise ValueError('k should be an integer between 1 and 52')
    if type(n) != int or n <= 0:
        raise TypeError('n should be a positive integer')
    suits = 0
    for i in range(0, n):
        h = 0
        s = 0
        d = 0
        c = 0
        hand = randomHand(deck, k)
        for card in hand:
            if card[0] == 'h':
                h = 1
            if card[0] == 's':
                s = 1
            if card[0] == 'd':
                d = 1
            if card[0] == 'c':
                c = 1
        suits = suits + h + s + d + c
    average = suits / n
    return average


def run(k, n):
    print(
        f'Average number of aces in hands of size {k} in {n} trials is {averageAces(k, n)}'
        )
    print(
        f'Average number of distinct suits in hands of size {k} in {n} trials is {averageSuits(k, n)}'
        )


createDeck()
if __name__ == '__main__':
    run(5, 100)
    assert 0.2 < averageAces(5, 100) < 0.6
