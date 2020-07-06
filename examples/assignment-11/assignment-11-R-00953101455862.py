import random


def createDeck():
    suits = ['Spade', 'Club', 'Heart', 'Diamond']
    faces = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    result = []
    for suit in suits:
        for face in faces:
            res = suit, face
            result.append(res)
    return result


def randomHand(deck, k):
    hand = []
    for i in range(k):
        drcard = random.choice(createDeck())
        hand.append(drcard)
    return hand


def averageAces(k, n):
    cnt = 0
    templist = []
    deck = createDeck()
    for i in range(n):
        templist.append(randomHand(deck, k))
    for a in templist:
        for b in a:
            if 'A' in b:
                cnt = cnt + 1
    average = cnt / n
    return average


def averageSuits(k, n):
    deck = createDeck()
    templist = []
    tot = []
    distinct = []
    length = 0
    avg = 0
    for i in range(n):
        templist.append(randomHand(deck, k))
    for j in templist:
        for card in j:
            length = length + 1
            if card[1] not in distinct:
                distinct.append(card[1])
            if length == len(j):
                tot.append(len(distinct))
        for k in tot:
            avg += k
        average = avg / n
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
