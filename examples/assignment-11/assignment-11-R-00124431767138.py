import random


def createDeck():
    values = [str(a) for a in range(1, 11)] + ['J', 'Q', 'K']
    suits = ['Club', 'Diamond', 'Heart', 'Spade']
    result = [[v, s] for v in values for s in suits]
    return result


def randomHand(deck, k):
    if k > 52 or k < 0:
        return None
    random.shuffle(deck)
    hand = deck[:k]
    return hand


def averageAces(k, n):
    if n <= 0:
        return None
    if k > 52 or k < 0:
        return None
    deck = createDeck()
    average = 0
    for i in range(n):
        hand = randomHand(deck, k)
        for card in hand:
            if '1' in card:
                average += 1
    average /= n
    return average


def averageSuits(k, n):
    if n <= 0:
        return None
    if k > 52 or k < 0:
        return None
    deck = createDeck()
    average = 0
    for i in range(n):
        hand = randomHand(deck, k)
        suits = set()
        for card in hand:
            suits.add(card[1])
        average += len(suits)
    average /= n
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
    assert averageAces(3, 0) == None
    assert averageSuits(3, 0) == None
    assert averageAces(0, 5) == 0
    assert averageSuits(0, 5) == 0
    assert averageAces(3, -2) == None
    assert averageSuits(3, -2) == None
    assert averageAces(-2, 5) == None
    assert averageSuits(-2, 5) == None
    assert averageAces(53, 5) == None
    assert averageSuits(53, 5) == None
