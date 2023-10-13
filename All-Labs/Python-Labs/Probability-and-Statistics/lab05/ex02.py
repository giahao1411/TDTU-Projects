import math
import numpy as np

# a
# let X = 0, 1, 2 is the head appear times
# x = [random.randint(0, 1) + random.randint(0, 1) for _ in range(10000)]
x = list(np.random.choice([0, 1, 2], 10000, p=[0.25, 0.5, 0.25]))
# print(x)
# print()

# b
X = set(x)
print(X)

# c
P = [x.count(i)/len(x) for i in X]
print("Probability distribute function =", P)

# d
EX = 0
for i in X:
    EX += i * P[i - 1]

print("Expectation =", EX)

VarX = 0
for i in X:
    VarX = VarX + (i - EX) ** 2 * P[i - 1]

print("Variance =", VarX)

SD = math.sqrt(VarX)
print("Standard deviation =", SD)

# e
P_at_least_one_head = sum(P[i] for i in X if i >= 1)
print("Probability that having at least one head =", P_at_least_one_head)
