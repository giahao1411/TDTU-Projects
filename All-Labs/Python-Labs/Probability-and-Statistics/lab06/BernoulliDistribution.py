import matplotlib.pyplot as plt
import math


def pmf_bernoulli(p, x):
    return math.pow(p, x) * math.pow(1 - p, 1 - x)


def plot_pmf_bernoulli(p):
    # Plot the probability mass function of Bernoulli(p)
    X = [0, 1]
    P_bernoulli = [pmf_bernoulli(p, x) for x in X]
    plt.plot(X, P_bernoulli, 'o')

    plt.title('PMF of Bernoulli(p = %.2f)' % (p))
    plt.xlabel('Value')
    plt.ylabel('Probability')
    plt.show()


plot_pmf_bernoulli(0.5)
