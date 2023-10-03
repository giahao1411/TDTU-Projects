import itertools
from fractions import Fraction


def cross(A, B):
    return {a + b for a in A for b in B}


def combos(items, n):
    return {' '.join(combo) for combo in itertools.combinations(items, n)}


urn = cross('W', '12345') | cross('B', '12') | cross('R', '123')

# print(urn)

U3 = combos(urn, 3)


def sameColours(U3):
    return {s for s in U3 if (s.count('W') or s.count('B') or s.count('R')) == 3}


def differentColours(U3):
    return {s for s in U3 if (s.count('W') or s.count('B') or s.count('R')) == 1}


def twoSameColours(U3):
    return {s for s in U3 if (s.count('W') or s.count('B') or s.count('R')) == 2}


def twoRedOneWhite(U3):
    return {s for s in U3 if (s.count('R') == 2 and s.count('W') == 1)}


def threeWhite(U3):
    print({s for s in U3 if s.count('W') == 3})

print()
print(len(sameColours(U3))/len(U3))
print(len(differentColours(U3))/len(U3))
print(len(twoSameColours(U3))/len(U3))
print(len(twoRedOneWhite(U3))/len(U3))
threeWhite(U3)

