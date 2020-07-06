import random


def createDeck():
    result = [[i, j] for j in range(13) for i in range(4)]
    return result


def randomHand(deck, k):
    hand = [[(0) for j in range(13)] for i in range(4)]
    x = random.sample(deck, k)
    for i in x:
        hand[i[0]][i[1]] = 1
    return hand


def averageAces(k, n):
    deck = createDeck()
    count = 0
    for i in range(n):
        a = randomHand(deck, k)
        for j in range(4):
            if a[j][12] == 1:
                count += 1
    average = count / n
    return average


def averageSuits(k, n):
    deck = createDeck()
    count = 0
    for i in range(n):
        a = randomHand(deck, k)
        for j in range(4):
            if sum(a[j]) >= 1:
                count += 1
    average = count / n
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
