import random


def createDeck():
    deck = []
    faces = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack',
        'queen', 'king']
    suits = ['clubs', 'diamonds', 'hearts', 'spades']
    for i in suits:
        for j in faces:
            deck.append([j, i])
    return deck


def randomHand(deck, k):
    hand = []
    shuffled = []
    shuffled = random.shuffle(deck)
    randomchoice = random.sample(range(0, 52), k)
    for i in randomchoice:
        hand.append(deck[i])
    return hand


def averageAces(k, n):
    deck = createDeck()
    aces = []
    sum = 0
    for i in range(0, n):
        hands = randomHand(deck, k)
        counter = 0
        for j in hands:
            if j[0] == 'ace':
                counter += 1
        aces.append(counter)
    for k in aces:
        sum = sum + k
    average = sum / n
    return average


def averageSuits(k, n):
    deck = createDeck()
    average = 0
    for i in range(0, n):
        suits = [0, 0, 0, 0]
        hands = randomHand(deck, k)
        counter = 0
        for j in hands:
            if j[1] == 'clubs':
                suits[0] = suits[0] + 1
            elif j[1] == 'diamonds':
                suits[1] = suits[1] + 1
            elif j[1] == 'spades':
                suits[2] = suits[2] + 1
            else:
                suits[3] = suits[3] + 1
        diff = 4
        for g in suits:
            if g == 0:
                diff = diff - 1
        average = average + diff
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
