import itertools
from fractions import Fraction

def cross(A, B):
    return {a + b for a in A for b in B}

def combos(items, n):
    return {' '.join(combo) for combo in itertools.combinations(items, n)}

urn = cross('W', '12345678') | cross('B', '123456') | cross('R', '123456789')

U6 = combos(urn, 6)

#8C2 * 6C2 * 9C2 / 23C6
w2b2r2 = {s for s in U6 if s.count('W') == 2 and s.count('B') == 2 and s.count('R') == 2}
print(len(w2b2r2)/len(U6))

