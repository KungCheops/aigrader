import random


def createDeck():
    ranks = [str(rank) for rank in range(2, 11)] + ['J', 'Q', 'K', 'A']
    suits = ['S', 'D', 'C', 'H']
    result = [(rank, suit) for suit in suits for rank in ranks]
    return result


def randomHand(deck, k):
    unused_cards = deck
    used_cards = []
    hand = []
    for i in range(k):
        drawn_card = random.choice(unused_cards)
        used_cards.append(drawn_card)
        unused_cards = [f for f in unused_cards if f not in used_cards]
        hand.append(drawn_card)
    return hand


def averageAces(k, n):
    number_of_aces = 0
    for trial in range(n):
        deck = createDeck()
        hand = randomHand(deck, k)
        for card in hand:
            if card[0] == 'A':
                number_of_aces += 1
    average = number_of_aces / n
    return average


def averageSuits(k, n):
    total_number_of_suits = 0
    for trial in range(n):
        deck = createDeck()
        hand = randomHand(deck, k)
        number_of_clubs = 0
        number_of_diamonds = 0
        number_of_hearts = 0
        number_of_spades = 0
        for card in hand:
            if card[1] == 'C':
                number_of_clubs += 1
            elif card[1] == 'D':
                number_of_diamonds += 1
            elif card[1] == 'H':
                number_of_hearts += 1
            else:
                number_of_spades += 1
        number_of_suits = 0
        suits = [number_of_clubs, number_of_diamonds, number_of_hearts,
            number_of_spades]
        for s in suits:
            if s > 0:
                number_of_suits += 1
        total_number_of_suits += number_of_suits
    average = total_number_of_suits / n
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
    assert 1 < averageSuits(5, 100) < 4
