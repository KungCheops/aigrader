import random


def createDeck():
    suits = ['hearts', 'diamonds', 'clubs', 'spades']
    ranks = ['ace', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
        'nine', 'ten', 'jack', 'queen', 'king']
    result = []
    for i in range(len(suits)):
        for j in range(len(ranks)):
            result.append(ranks[j] + ' of ' + suits[i])
    return result


def randomHand(deck, k):
    hand = []
    random.shuffle(deck)
    for i in range(k):
        hand.append(deck[i])
    return hand


def averageAces(k, n):
    deck = createDeck()
    average = 0
    for i in range(n):
        hand = randomHand(deck, k)
        average += sum('ace' in s for s in hand)
    average /= n
    return average


def averageSuits(k, n):
    deck = createDeck()
    average = 0
    num_suits = 0
    for i in range(n):
        hand = randomHand(deck, k)
        for s in hand:
            if 'hearts' in s:
                num_suits += 1
                break
        for s in hand:
            if 'diamonds' in s:
                num_suits += 1
                break
        for s in hand:
            if 'clubs' in s:
                num_suits += 1
                break
        for s in hand:
            if 'spades' in s:
                num_suits += 1
                break
        average += num_suits
        num_suits = 0
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
