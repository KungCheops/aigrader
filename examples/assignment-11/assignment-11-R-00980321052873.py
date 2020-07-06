import random


def createDeck():
    rank = ['a', 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    suit = [1, 2, 3, 4]
    result = []
    for s in suit:
        for n in rank:
            result.append([s, n])
    return result


def randomHand(deck, k):
    hand = []
    for n in range(k):
        hand.append(deck.pop(random.randrange(0, len(deck))))
    return hand


def averageAces(k, n):
    acelist = []
    for i in range(n):
        aces = 0
        deck = createDeck()
        hand = randomHand(deck, k)
        for h in hand:
            if 'a' in h:
                aces = aces + 1
        acelist.append(aces)
    average = sum(acelist) / len(acelist)
    return average


def averageSuits(k, n):
    distinct = []
    for i in range(n):
        deck = createDeck()
        hand = randomHand(deck, k)
        suitSet = set([])
        for h in hand:
            suitSet.add(h[0])
        distinct.append(len(suitSet))
    average = sum(distinct) / len(distinct)
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
