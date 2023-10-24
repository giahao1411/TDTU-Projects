import matplotlib.pyplot as plt
import math


def pmf_geo(p, x):
    return p * (1 - p)**x


# a
print("a. probability that the person hits the target in the third try = ", pmf_geo(0.4, 2))

# b
print("b. ")


def plot_pmf_geo(p):
    # Plot the probability mass function of Geometric
    X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    P_geo = [pmf_geo(p, x) for x in X]
    plt.plot(X, P_geo, '-o')
    plt.title('PMF of Geometric(%.2f)' % p)
    plt.xlabel('Number of tries')
    plt.ylabel('Probability of Number of tries')
    plt.show()


plot_pmf_geo(0.4)
