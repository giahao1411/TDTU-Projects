import random
from itertools import *

Ranks = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'}
Suits = {'♡', '♢', '♣', '♠'}
Cards = list(product(Ranks , Suits))

#5 cards are heart -> (13C5)/52C5 
def simulator_poker1(n):
    count = 0 
    for i in range(n):
        hand = random.sample(Cards, 5)
        if sum(cards[1] == '♡' for cards in hand) == 5:
            count += 1
    return count

#4 different cards 1 diamond, 1 heart, 1 club, 1 spade -> (13C1^4)/52C4 
def simulator_poker2(n):
    count = 0
    for i in range(n):
        hand = random.sample(Cards, 4)
        if len(set(cards[1] for cards in hand)) == 4:
            count += 1
    return count

n = 100000
print("5 cards are heart: ", simulator_poker1(n)/n)
print("4 different cards: ", simulator_poker2(n)/n)
        