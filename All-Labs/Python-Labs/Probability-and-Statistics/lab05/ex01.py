import numpy as np
import math

x = list(np.random.choice([0, 1, 2, 3, 4, 5], 3650, p=[
    0.1, 0.2, 0.3, 0.2, 0.15, 0.05]))

# a
X = set(x)
print(X)
print()

# b
P = [x.count(value)/len(x) for value in X]
print("Probability distribution function =", P)
print()

# c
# Expectation
EX = 0
for x in X:
    EX = EX + (x * P[x - 1])

print("Expectation =", EX)
print()

# Variance
VarX = 0
for x in X:
    VarX = VarX + (x - EX) * (x - EX) * P[x - 1]

print("Variance =", VarX)
print()

# Standard Deviation
SD = math.sqrt(VarX)
print("Standard deviation =", SD)
print()

P3 = sum(P[i] for i in X if i >= 3)
print("Probability that having 3 or more emergency cases =", P3)
