import random


def createDeck():
    result = []
    rank = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    suit = ['Heart', 'Diamond', 'Spade', 'Club']
    for a in suit:
        for b in rank:
            result.append([a, b])
    return result


def randomHand(deck, k):
    hand = []
    for c in range(k):
        hand.append(random.choice(deck))
    return hand


def averageAces(k, n):
    aces = 0
    for i in range(n):
        deck = createDeck()
        hand = randomHand(deck, k)
        for h in hand:
            if 'A' in h:
                aces = aces + 1
    average = aces / n
    return average


def averageSuits(k, n):
    unique = []
    for i in range(n):
        deck = createDeck()
        hand = randomHand(deck, k)
        suitS = set([])
        for han in hand:
            suitS.add(han[0])
        unique.append(len(suitS))
    average = sum(unique) / len(unique)
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
