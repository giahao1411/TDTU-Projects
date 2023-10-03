import random
from itertools import *

Ranks = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'}
Suits = {'♡', '♢', '♣', '♠'}
Cards = list(product(Ranks, Suits))


def hand4Cards():
    return random.sample(Cards, 4)


def fourSameSuit(n):
    count = 0
    for i in range(n):
        hand = hand4Cards()
        if len(set(card[1] for card in hand)) == 1:
            count += 1
    return count


def fourDifferentSuit(n):
    count = 0
    for i in range(n):
        hand = hand4Cards()
        if len(set(card[1] for card in hand)) == 4:
            count += 1
    return count


def fourSameColours(n):
    count = 0
    redSuit = {'♡', '♢'}
    blackSuit = {'♣', '♠'}
    for i in range(n):
        hand = hand4Cards()
        if all(card[1] in redSuit for card in hand) or all(card[1] in blackSuit for card in hand):
            count += 1
    return count


def fourSameValues(n):
    count = 0
    for i in range(n):
        hand = hand4Cards()
        if all(card[0] == hand[0][0] for card in hand):
            count += 1
    return count


def fourAreNumbers(n):
    count = 0
    faces = {'J', 'Q', 'K', 'A'}
    for i in range(n):
        hand = hand4Cards()
        if all(card[0] not in faces for card in hand):
            count += 1
    return count


def fourAreFaces(n):
    count = 0
    faces = {'J', 'Q', 'K', 'A'}
    for i in range(n):
        hand = hand4Cards()
        if all(card[0] in faces for card in hand):
            count += 1
    return count


n = 100000
print(fourSameSuit(n)/n)
print(fourDifferentSuit(n)/n)
print(fourSameColours(n)/n)
print(fourSameValues(n)/n)
print(fourAreNumbers(n)/n)
print(fourAreFaces(n)/n)
