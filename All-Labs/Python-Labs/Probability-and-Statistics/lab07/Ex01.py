from NormalDistribution import *


def plot_cdf_normal(mu, sigma):
    # Plot the Cumulative distributioin fucntion of Normal(mu, sigma)
    X = generator_data(mu - 4 * sigma, mu + 4 * sigma, 1000)
    P_normal = [cdf_normal(x, mu, sigma) for x in X]
    plt.plot(X, P_normal, '-')
    plt.title('CDF of Normal(%.2f, %.2f)' % (mu, sigma))
    plt.xlabel('X')
    plt.ylabel('P')
    plt.show()


plot_cdf_normal(0, 1.5)
