import random
import math


# compute the expectation of an r.v
# X is the r.v and P is the prob distribution of X
def Expectation(X, P):
    EX = 0
    for i in X:
        EX += i * P[i - 1]
    return EX


# compute the variance of an r.v
def Variance(X, P, mu):
    Var = 0
    for i in X:
        Var += math.pow(i - mu, 2) * P[i - 1]
    return Var


# compute the standard deviation of an r.v
def Standard_Deviation(Variance):
    return math.sqrt(Variance)


# flipping the 2 dices 10000 times and store them to the x which is the summation of both dices
x = [random.randint(1, 6) + random.randint(1, 6) for _ in range(10000)]

# find the r.v of x then store them to X
X = set(x)
# print(X)

# compute the probability distribution function of X then store them to P
P = [x.count(s) / len(x) for s in x]

# expectation
Expectation = Expectation(X, P)
# print("Expectation = ", Expectation)

# variance
Variance = Variance(X, P, Expectation)
# print("Variance = ", Variance)

# standard deviation
Standard_Deviation = Standard_Deviation(Variance)
# print("Standard Deviation = ", Standard_Deviation)
