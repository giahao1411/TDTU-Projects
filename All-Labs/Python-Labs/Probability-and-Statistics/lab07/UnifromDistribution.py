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


def pmf_uniform_cont(a, b):
    return 1 / (b - a)


def plot_pmf_uniform_cont(a, b):
    # Plot the probability mass function of Uniform(a, b)

    X = generator_data(a, b, 100)
    if b != a:
        P = [pmf_uniform_cont(a, b) for x in X]

    plt.plot(X, P, '-')
    plt.plot([a, a], [0, 1/(b-a)], 'g--')
    plt.plot([b, b], [0, 1/(b-a)], 'g--')

    plt.title('PDF of Uniform continuous distribution(%0.2f, %0.2f)' % (a, b))
    plt.show()


plot_pmf_uniform_cont(4, 6)
