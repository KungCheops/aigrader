import random


def createDeck():
    card_deck = []
    suits = 'Diamonds', 'Clubs', 'Hearts', 'Spades'
    numbers = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack',
        'Queen', 'King')
    for s in suits:
        for n in numbers:
            card_deck.append(n + ' ' + s)
    return card_deck


def randomHand(deck, k):
    random.shuffle(deck)
    hand = deck[:k]
    return hand


def averageAces(k, n):
    deck = createDeck()
    ace_count = 0
    for i in range(0, n + 1):
        hand = randomHand(deck, k)
        for h in hand:
            if 'Ace' in h:
                ace_count += 1
    average = ace_count / n
    return average


def averageSuits(k, n):
    deck = createDeck()
    suit_count_int = 0
    for i in range(0, n + 1):
        hand = randomHand(deck, k)
        has_heart = False
        has_spade = False
        has_club = False
        has_diamond = False
        for h in hand:
            if 'Heart' in h:
                has_heart = True
            elif 'Spade' in h:
                has_spade = True
            elif 'Club' in h:
                has_club = True
            else:
                has_diamond = True
        suit_count = has_heart + has_spade + has_club + has_diamond
        suit_count_int = suit_count_int + suit_count
    average = suit_count_int / n
    return average


def run(k, n):
    print(
        'Average number of aces in hands of size {k} in {n} trials is {averageAces(k, n)}'
        )
    print(
        'Average number of distinct suits in hands of size {k} in {n} trials is {averageSuits(k, n)}'
        )


if __name__ == '__main__':
    run(5, 100)
    assert 0.2 < averageAces(5, 100) < 0.6
    assert 1 < averageSuits(3, 100) < 4
