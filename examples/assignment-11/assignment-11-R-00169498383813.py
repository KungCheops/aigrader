import random


def createDeck():
    suits = ['Spade', 'Club', 'Heart', 'Diamond']
    faces = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']
    result = []
    for suit in suits:
        for face in faces:
            result.append((face, suit))
    return result


def randomHand(deck, k):
    deck = createDeck()
    hand = []
    random.shuffle(deck)
    for i in range(k):
        hand.append(deck[i])
    return hand


def averageAces(k, n):
    count = 0
    templist = []
    deck = createDeck()
    for i in range(n):
        templist.append(randomHand(deck, k))
    for x in templist:
        for y in x:
            if 'Ace' in y:
                count = count + 1
    average = count / n
    return average


def averageSuits(k, n):
    templist = []
    resultset = []
    distinct = []
    length = 0
    total = 0
    deck = createDeck()
    for i in range(n):
        templist.append(randomHand(deck, k))
    for sett in templist:
        distinct = []
        length = 0
        for card in sett:
            length = length + 1
            if card[1] not in distinct:
                distinct.append(card[1])
            if length == len(sett):
                resultset.append(len(distinct))
    for k in resultset:
        total += k
    average = total / n
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
