import random


def createDeck():
    result = {'c02', 'c03', 'c04', 'c05', 'c06', 'c07', 'c08', 'c09', 'c10',
        'cj', 'cq', 'ck', 'ca', 'd02', 'd03', 'd04', 'd05', 'd06', 'd07',
        'd08', 'd09', 'd10', 'dj', 'dq', 'dk', 'da', 's02', 's03', 's04',
        's05', 's06', 's07', 's08', 's09', 's10', 'sj', 'sq', 'sk', 'sa',
        'h02', 'h03', 'h04', 'h05', 'h06', 'h07', 'h08', 'h09', 'h10', 'hj',
        'hq', 'hk', 'ha'}
    return result


def randomHand(deck, k):
    hand = random.sample(deck, k)
    return hand


def averageAces(k, n):
    deck = createDeck()
    c = 0
    for i in range(n):
        l = randomHand(deck, k)
        for j in l:
            if j[1] == 'a':
                c = c + 1
    average = c / n
    return average


def averageSuits(k, n):
    deck = createDeck()
    c = 0
    suits = [0, 0, 0, 0]
    T = []
    for i in range(n):
        l = randomHand(deck, k)
        for j in l:
            if j[0] == 'c':
                suits[0] = 1
            elif j[0] == 'h':
                suits[1] = 1
            elif j[0] == 's':
                suits[2] = 1
            else:
                suits[3] = 1
        s = suits[0] + suits[1] + suits[2] + suits[3]
        T.append(s)
        suits = [0, 0, 0, 0]
    for k in T:
        c = c + k
    average = c / n
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
