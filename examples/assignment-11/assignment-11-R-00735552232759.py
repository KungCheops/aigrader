import random


def createDeck():
    cards = []
    result = []
    suits = ['Hearts', 'Spades', 'Diamonds', 'Clubs']
    royals = ['J', 'Q', 'K', 'Ace']
    for i in range(2, 11):
        cards.append(str(i))
    for j in range(4):
        cards.append(royals[j])
    for k in range(4):
        for l in range(13):
            result.append(str(suits[k] + cards[l]))
    return result


def randomHand(deck, k):
    random.shuffle(deck)
    hand = []
    for i in range(k):
        number = random.randint(0, 51)
        hand.append(deck[number])
    return hand


def averageAces(k, n):
    deck = createDeck()
    result = []
    count = 0
    for j in range(n):
        result = randomHand(deck, k)
        for i in range(k):
            if result[i].endswith('Ace'):
                count += 1
    average = count / n
    return average


def averageSuits(k, n):
    deck = createDeck()
    suits = ['Hearts', 'Spades', 'Diamonds', 'Clubs']
    average = 0
    result = []
    count = [0, 0, 0, 0]
    sum = 0
    for j in range(n):
        result = randomHand(deck, k)
        count = [0, 0, 0, 0]
        for i in range(k):
            for m in range(4):
                if result[i].startswith(suits[m]):
                    count[m] = 1
        for r in range(4):
            sum += count[r]
        average = sum / n
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
