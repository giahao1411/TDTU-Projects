from fractions import Fraction
from itertools import *
import random


def P(event, space):
    # The probability of an event, given a sample space of equiprotable outcomes.
    return Fraction(len(event & space), len(space))


D = {1, 2, 3, 4, 5, 6}
even = {2, 4, 6}

# print(P(even, D))


def cross(A, B):
    return {a + b for a in A for b in B}


urn = cross('W', '12345678') | cross('B', '123456') | cross('R', '123456789')

# print(urn)


def combos(items, n):
    # All combinations of n items; each combo as a concatenated str
    return {' '.join(combo) for combo in combinations(items, n)}

U6 = combos(urn, 6)

# print(len(U6))

# print(random.sample(list(U6), 10))

#case Red balss
red6 = {s for s in U6 if s.count('R') == 6}
print(P(red6, U6))

#case 3 blue, 2 white and 1 red
b3w2r1 = {s for s in U6 if s.count('B') == 3 and s.count('w') == 2 and s.count('R') == 1}
# print(P(b3w2r1, U6))

#case exactly 4 white balls
w4 = {s for s in U6 if s.count('W') == 4}
# print(P(w4, U6))

#coin experiment
n = 10
count = 0

for simulations in range(n):
    tosses = random.randint(0, 1)
    if tosses == 1:
        count += 1

# print(count/n)

#dice experiment
import random
count = 0
n = 1000000

for i in range(n):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    if die1==1 and die2==6:
        count += 1

# print(count/n)

#cards experiment
# Define ranks , suits and cards
Ranks = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'}
Suits = {'♡', '♢', '♣', '♠'}
Cards = list(product(Ranks , Suits))
# print(len(Cards))
# print(Cards[:10])

def simulator_poker(n):
    count = 0
    for i in range(n):
        index = random.randint(0, 51)
        if Cards[index][1] == '♡' or Cards[index][1] == '♢':
            count += 1
    return count/n

# print(simulator_poker(10))
# print(simulator_poker(100))
# print(simulator_poker(1000))
# print(simulator_poker(10000))