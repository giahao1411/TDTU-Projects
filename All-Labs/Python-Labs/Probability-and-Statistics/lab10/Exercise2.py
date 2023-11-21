from Exercise1 import *
import matplotlib.pyplot as plt


# compute the probability mass function of the normal distribution
def pmf_normal(x, mu, sigma):
    pmf = (
        1
        / math.sqrt(2 * math.pi * math.pow(sigma, 2))
        * math.exp(-math.pow(x - mu, 2) / 2 * math.pow(sigma, 2))
    )
    return pmf


# compute the cummulative density function of the normal distribution
def cdf_normal(x, mu, sigma):
    cdf = 1 / 2 * (1 + math.erf((x - mu) / sigma * pow(2, 1 / 2)))
    return cdf


# generator data function
def generator_data(a, b, size):
    n = (b - a) / (size - 1)
    result = []
    s = a
    while s < b:
        result.append(s)
        s = s + n
    if len(result) < size:
        result.append(b)
    return result


# plot the relationship between X and pmf
def plot_pmf_normal(mu, sigma):
    X = generator_data(mu - 4 * sigma, mu + 4 * sigma, 1000)
    P_normal = [pmf_normal(x, mu, sigma) for x in X]
    plt.plot(X, P_normal, "-")
    plt.title("PMF of Normal(%.2f, %.2f)" % (mu, sigma))
    plt.xlabel("X")
    plt.ylabel("P")
    plt.show()


# plot the relationship between X and cdf
def plot_cdf_normal(mu, sigma):
    X = generator_data(mu - 4 * sigma, mu + 4 * sigma, 1000)
    P_normal = [cdf_normal(x, mu, sigma) for x in X]
    plt.plot(X, P_normal, "-")
    plt.title("CDF of Normal(%.2f, %.2f)" % (mu, sigma))
    plt.xlabel("X")
    plt.ylabel("P")
    plt.show()


# plot_pmf_normal(Expectation, Standard_Deviation)
# plot_cdf_normal(Expectation, Standard_Deviation)

# having mu = 3, sigma^2 = 16. Find P{2 < X < 7}
cdf_7 = cdf_normal(7, 3, 16)
cdf_2 = cdf_normal(2, 3, 16)
print("2 < P < 7 = %.4f" % (cdf_7 - cdf_2))
