from fractions import Fraction


def P(event, space):
    return Fraction(len(event & space), len(space))


S = {'MMM', 'MMF', 'MFM', 'FMM', 'MFF', 'FMF', 'FFM', 'FFF'}

print("a. Sample space is: ", S)
print("b. Sample space size: ", len(S))

# let B is the event that has at least one female cat
B = {s for s in S if 'F' in s}
print("c. Event sample space: ", B, " - size: ", len(B))

# let A is the event that three cats are female
A_B = {s for s in B if s.count('F') == 3}
print("d. Event sample space: ", A_B, " - size: ", len(A_B))

P_B = P(B, S)
P_A_B = P(A_B, S)

P_A_with_B = P_A_B / P_B
print("Prob 3 female cats under condition has at least one female cat: ", P_A_with_B)
