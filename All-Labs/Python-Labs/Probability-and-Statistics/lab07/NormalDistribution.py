import math
import matplotlib.pyplot as plt


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


def pmf_normal(x, mu, sigma):
    return (1 / math.sqrt(2 * math.pi * math.pow(sigma, 2))) * math.exp(- math.pow(x - mu, 2) / (2 * math.pow(sigma, 2)))


def cdf_normal(x, mu, sigma):
    return 1/2 * (1 + math.erf((x - mu) / math.pow(sigma, 1/2)))


def plot_pdf_normal(mu, sigma):
    # Plot the probability mass function of Normal(mu, sigma)

    X = generator_data(mu - 4 * sigma, mu + 4 * sigma, 1000)
    P_normal = [pmf_normal(x, mu, sigma) for x in X]
    plt.plot(X, P_normal, '-')
    plt.title('PMF of Normal(%.2f, %.2f)' % (mu, sigma))
    plt.xlabel('X')
    plt.ylabel('P')
    plt.show()


plot_pdf_normal(0, 1.5)
