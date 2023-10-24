import matplotlib.pyplot as plt
import math


def combination(n, k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))


def pmf_binom(k, n, p):
    return combination(n, k) * p**k * (1 - p)**(n - k)


# a
print("a. probability of 2 machines are broken = ", pmf_binom(3, 5, 0.9))

# b
print("b. \n")


def plot_pmf_binom(n, p):
    # Plot the probability mass function of Binom(n, p)
    X = [0, 1, 2, 3, 4, 5]
    P_binom = [pmf_binom(x, n, p) for x in X]
    plt.plot(X, P_binom, '-o')
    axes = plt.gca()
    axes.set_xlim([0, n])
    axes.set_ylim([0, 1.1 * max(P_binom)])

    plt.title('PMF of Bin(%i, %.2f)' % (n, p))
    plt.xlabel('Number k of successes')
    plt.ylabel('Probability of k successes')
    plt.show()


plot_pmf_binom(5, 0.9)
