import itertools
from fractions import Fraction


def cross(A, B):
    return {a + b for a in A for b in B}


def combos(items, n):
    return {' '.join(combo) for combo in itertools.combinations(items, n)}


URN = cross('W', '12') | cross('B', '123') | cross('R', '1234')

# print(urn)


U3 = combos(URN, 3)
# print(b)

# c
white1blue1red1 = {s for s in U3 if s.count(
    'W') == 1 and s.count('B') == 1 and s.count('R') == 1}
print(white1blue1red1)

# d
print("\nProbability of white1blue1red1 =", len(white1blue1red1)/len(U3))
