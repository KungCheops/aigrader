import random


def createDeck():
    result = []
    for rank in range(13):
        for suit in ['hearts', 'spades', 'diamonds', 'clubs']:
            result.append(str(rank + 1) + ' of ' + suit)
    random.shuffle(result)
    return result


def randomHand(deck, k):
    hand = []
    for i in range(k):
        hand.append(random.choice(deck))
    return hand


def averageAces(k, n):
    deck = createDeck()
    counter = 0
    for i in range(n):
        hand = randomHand(deck, k)
        for card in hand:
            if card.startswith('1 '):
                counter += 1
    average = counter / n
    return average


def averageSuits(k, n):
    deck = createDeck()
    counter = 0
    for i in range(n):
        distinctsuits = []
        hand = randomHand(deck, k)
        for card in hand:
            if getSuit(card) not in distinctsuits:
                distinctsuits.append(getSuit(card))
                counter += 1
    average = counter / n
    return average


def getSuit(card):
    if 'spade' in card:
        return 'spade'
    elif 'heart' in card:
        return 'heart'
    elif 'diamond' in card:
        return 'diamond'
    else:
        return 'club'


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
