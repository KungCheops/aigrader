from enum import Enum
import random
import logging
logging.basicConfig(level=logging.INFO)


class Suite(Enum):
    DIAMONDS = 0
    CLUBS = 1
    HEARTS = 2
    SPADES = 3


def createDeck():
    result = {i.name: list(range(1, 14)) for i in Suite}
    logging.debug(result)
    return result


def randomHand(deck, k):
    if k < 1 or k > 52:
        logging.debug('Empty Hand')
        return {}
    elif k == 52:
        logging.debug('The hand is the deck')
        return deck
    else:
        hand = {}
        hand_size = 0
        while hand_size != k:
            suite = Suite(random.randint(0, 3)).name
            if len(deck[suite]) > 0:
                card_position = random.randint(0, len(deck[suite]) - 1)
                card_number = deck[suite][card_position]
                del deck[suite][card_position]
                hand_size += 1
                logging.debug(hand_size)
                logging.debug('Suite: ' + str(suite))
                logging.debug('card_number: ' + str(card_number))
                logging.debug('----')
                if suite not in hand:
                    hand[suite] = [card_number]
                else:
                    hand[suite].append(card_number)
        return hand


def averageAces(k, n):
    hands = []
    average = 0
    ACE = 1
    aces_per_hand = []
    if k < 1 or k > 52 or n < 1:
        return 0.0
    hands = [randomHand(createDeck(), k) for i in range(0, n)]
    for hand in hands:
        number_of_aces = 0
        for suite in list(hand.keys()):
            if ACE in hand[suite]:
                number_of_aces += 1
        aces_per_hand.append(number_of_aces)
    logging.debug('>> Aces per hand = ' + str(aces_per_hand))
    average = float(sum(aces_per_hand)) / float(len(aces_per_hand))
    return float(average)


def averageSuits(k, n):
    hands = []
    average = 0
    suites_per_hand = []
    if k < 1 or k > 52 or n < 1:
        return 0.0
    hands = [randomHand(createDeck(), k) for i in range(0, n)]
    for hand in hands:
        suites_per_hand.append(len(list(hand.keys())))
    logging.debug('>> Suites per hand = ' + str(suites_per_hand))
    average = float(sum(suites_per_hand)) / float(len(suites_per_hand))
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
