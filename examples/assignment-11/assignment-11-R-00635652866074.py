import random


def createDeck():
    ranks = ['Club', 'Diamond', 'Heart', 'Spade']
    suits = ['Ace', 'King', 'Queen', 'Jack'] + list(range(2, 11))
    result = [(rank, suit) for rank in ranks for suit in suits]
    return result


def randomHand(deck, k):
    hand = []
    for i in random.sample(range(0, len(deck)), k):
        hand.append(deck[i])
    return hand


def averageAces(k, n):
    deck = createDeck()
    count = 0
    for i in range(0, n):
        hand = randomHand(deck, k)
        for x in hand:
            if x[1] == 'Ace':
                count += 1
    average = count / n
    return average


def averageSuits(k, n):
    deck = createDeck()
    suits = set()
    for i in range(0, n):
        hand = randomHand(deck, k)
        for x in hand:
            suits.add(x[0])
    average = len(suits)
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
    assert len(createDeck()) == 52
    assert len(randomHand(createDeck(), 5)) == 5
