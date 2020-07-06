import random


def createDeck():
    card_nums = []
    for i in range(2, 15):
        if i < 11:
            card_nums.append(i)
        elif i == 11:
            card_nums.append('J')
        elif i == 12:
            card_nums.append('D')
        elif i == 13:
            card_nums.append('K')
        else:
            card_nums.append('A')
    card_colors = {'heart', 'spade', 'diamond', 'club'}
    result = [[num, color] for num in card_nums for color in card_colors]
    return result


def randomHand(deck, k):
    hand = random.sample(deck, k)
    return hand


def averageAces(k, n):
    deck = createDeck()
    ace_num = 0
    for i in range(n):
        hand = randomHand(deck, k)
        for j in hand:
            if j[0] == 'A':
                ace_num += 1
    average = ace_num / n
    return average


def averageSuits(k, n):
    deck = createDeck()
    suits_num = 0
    for i in range(n):
        suits = {'heart': 0, 'spade': 0, 'diamond': 0, 'club': 0}
        hand = randomHand(deck, k)
        for j in hand:
            suits[j[1]] += 1
        for m in suits:
            if suits[m] != 0:
                suits_num += 1
    average = suits_num / n
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
