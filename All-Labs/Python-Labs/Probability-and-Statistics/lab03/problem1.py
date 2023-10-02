from fractions import Fraction


def P(event, space):
    return Fraction(len(event & space), len(space))


S = {'BB', 'BG', 'GB', 'GG'}

# let B is a sample space that has at least one children is a boy
B = {s for s in S if 'B' in s}

# let A_B is sample space that has 2 boys - intersection of A and B
A_B = {s for s in B if s.count('B') == 2}

P_B = P(B, S)
P_A_B = P(A_B, S)

# P(A|B) = P(A intersection B)) / P(B)
P_A_with_B = P_A_B / P_B
print(P_A_with_B)
