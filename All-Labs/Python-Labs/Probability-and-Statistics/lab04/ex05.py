import random
from itertools import *
from math import *

Ranks = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'}
Suits = {'♡', '♢', '♣', '♠'}
Cards = list(product(Ranks, Suits))


def hand5Cards():
    return random.sample(Cards, 5)


def possibleStraight():
    numOfStraights = 10
    numOfSuits = 4
    numOfCards = 5
    return numOfStraights * numOfSuits ** numOfCards


def is_straight(hand):
    ranks = [card[0] for card in hand]
    return sorted(ranks) in (list(range(i, i + 5)) for i in range(1, 11))


def theorical():
    straightEvent = possibleStraight()
    sampleSpace = len(list(combinations(Cards, 5)))
    print("Theorical probability:", straightEvent/sampleSpace)


def practical(n):
    count = 0
    for i in range(n):
        deck = list(product(range(1, 14), '♡♢♣♠'))
        hand = random.sample(deck, 5)
        if is_straight(hand):
            count += 1
    print("Practical probability:", count/n)


theorical()
practical(100000)
