import matplotlib.pyplot as plt
import math


def pmf_poisson(k, lam):
    return (lam**k * math.exp(-lam)) / math.factorial(k)


# a
print("a. probability that center receives 2 calls in 1 minute = ", pmf_poisson(2, 3))

# b
print("b.")


def plot_pmf_poisson(lam):
    # Plot the probability mass function  of Poisson(n, lambda)
    X = [1, 2, 3, 4, 5]
    P_poisson = [pmf_poisson(x, lam) for x in X]
    plt.plot(X, P_poisson, '-o')
    plt.title('PMF of Poisson(%i)' % lam)
    plt.xlabel('Number of Events')
    plt.ylabel('Probability of Number of Events')
    plt.show()


plot_pmf_poisson(3)
