from random import randint


def createDeck():
    """
    Returns a fresh set of 52 (ordered) cards, with 4 suits and 13 values in 
    each suit.
    """
    suite = ['h', 's', 'c', 'd']
    value = ['a', 'k', 'q', 'j', '10', '9', '8', '7', '6', '5', '4', '3', '2']
    result = [(s + '_' + v) for v in value for s in suite]
    return result


def randomHand(deck, k):
    """
    Randomly picks a card k times from a deck of cards.
    """
    hand = []
    deck_size = len(deck) - 1
    for i in range(k):
        card_no = randint(0, deck_size - 1 - i)
        hand.append(deck[card_no])
        del deck[card_no]
    return hand


def averageAces(k, n):
    """
    Creates a deck, deals a hand of k randomely picked cards. This is repeated
    n times and every time, the number of aces given is added to a total.
    Returns the average number of aces in a hand based on n trials.
    """
    aces = 0
    try:
        for i in range(n):
            deck = createDeck()
            hand = randomHand(deck, k)
            for card in hand:
                if '_a' in card:
                    aces += 1
        average = aces / n
        return average
    except:
        print('There is something wrong with the input.')
        print('Rules are: k must be integer less then 52, n must be integer.')
        print('Give it a try again!')


def averageSuits(k, n):
    """
    Creates a deck, deals a hand of k randomely picked cards. This is repeated
    n times and every time, the number of suits given is added to the total.
    Returns the average number of suits in a hand based on n trials.
    """
    suits_count = 0
    try:
        for i in range(n):
            deck = createDeck()
            hand = randomHand(deck, k)
            suits = [[j for j in hand if 'h_' in j], [j for j in hand if 
                's_' in j], [j for j in hand if 'c_' in j], [j for j in
                hand if 'd_' in j]]
            for s in suits:
                if len(s) > 0:
                    suits_count += 1
        average = suits_count / n
        return average
    except:
        print('There is something wrong with the input.')
        print('Rules are: k must be integer less then 52, n must be integer.')
        print('Give it a try again!')


def run(k, n):
    """
    I wanted to change this function to something that suits my soution
    better but since I'm not allowed...;)
    """
    print(
        f'Average number of aces in hands of size {k} in {n} trials is {averageAces(k, n)}'
        )
    print(
        f'Average number of distinct suits in hands of size {k} in {n} trials is {averageSuits(k, n)}'
        )


if __name__ == '__main__':
    run(5, 100000)
    assert 0.2 < averageAces(5, 100) < 0.6
