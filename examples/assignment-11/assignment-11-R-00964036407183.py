import random
CLUBS = 'clubs'
SPADES = 'spades'
DIAMONDS = 'diamonds'
HEARTS = 'hearts'


def createDeck():
    suits = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']
    generate = lambda type: [(type, card) for card in suits]
    deck = generate(CLUBS) + generate(DIAMONDS) + generate(HEARTS) + generate(
        SPADES)
    random.shuffle(deck)
    return deck


def randomHand(deck, k):
    hand = random.sample(deck, k)
    return hand


def averageAces(k, n):
    deck = createDeck()
    count = 0
    for i in range(n):
        count += sum([(card_type == 'Ace') for _, card_type in randomHand(
            deck, k)])
    average = count / n
    return average


def averageSuits(k, n):
    deck = createDeck()
    count_diff = lambda hand: len(set([s for s, _ in hand]))
    count = 0
    for i in range(n):
        r_hand = randomHand(deck, k)
        count = count + count_diff(r_hand)
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
