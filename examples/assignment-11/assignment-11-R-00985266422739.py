import random
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
values = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']


def createDeck():
    deck = []
    for s in suits:
        for v in values:
            card = v, s
            deck.append(card)
    return deck


def randomHand(deck, k):
    random.shuffle(deck)
    hand = deck[:k]
    return hand


def averageAces(k, n):
    deck = createDeck()
    average = 0
    i = 0
    while i != n:
        hand = randomHand(deck, k)
        handAverage = 1
        aceCount = 0
        deckSize = 52
        for card in hand:
            if 'Ace' in card:
                aceCount += 1
        i += 1
        average = average + aceCount
    average = average / n
    return average


def averageSuits(k, n):
    deck = createDeck()
    average = 0
    i = 0
    while i != n:
        hand = randomHand(deck, k)
        handAverage = 1
        distinctSuit = 0
        deckSize = 52
        diamond = False
        heart = False
        club = False
        spade = False
        for card in hand:
            if 'Diamonds' in card and diamond == False:
                distinctSuit += 1
                diamond = True
            elif 'Hearts' in card and heart == False:
                distinctSuit += 1
                heart = True
            elif 'Spades' in card and spade == False:
                distinctSuit += 1
                spade = True
            elif 'Clubs' in card and club == False:
                distinctSuit += 1
                club = True
        i += 1
        average = average + distinctSuit
    average = average / n
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
