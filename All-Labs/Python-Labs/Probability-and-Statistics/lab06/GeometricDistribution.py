import matplotlib.pyplot as plt
import math


def pmf_geo(p, x):
    return p * (1 - p)**x


def plot_pmf_geo(p, n):
    # Plot the probability mass function of Geometric
    X = list(range(0, n + 1))
    P_geo = [pmf_geo(p, x) for x in X]
    plt.plot(X, P_geo, '-o')
    plt.title('PMF of Geometric(%. 2f)' % p)
    plt.xlabel('Number of tries')
    plt.ylabel('Probability of Number of tries')
    plt.show()


plot_pmf_geo(0.3, 10)
