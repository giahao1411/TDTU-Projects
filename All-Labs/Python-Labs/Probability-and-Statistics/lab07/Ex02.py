import math


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
    return 1 / 2 * (1 + math.erf((x - mu) / (sigma * math.sqrt(2))))


cdf_9 = cdf_normal(9, 10, 1)
cdf_12 = cdf_normal(12, 10, 1)


print("Probability = %.4f" % (cdf_12 - cdf_9))

# cdf_12 = 0.9772
# cdf_9 = 0.1587
# Probability that the product will be generated in the period from 9 to 12 minutes is cdf_12 - cdf_9 = 0.8186

# 1. P(Z < 1.51)
print("1. Result = %.4f" % cdf_normal(1.51, 0, 1))

# 2. P(Z < 2.13)
print("2. Result = %.4f" % cdf_normal(2.13, 0, 1))

# 3. P(Z < -0.87)
print("3. Result = %.4f" % cdf_normal(-0.87, 0, 1))

# 4. P(Z < 1.11)
print("4. Result = %.4f" % (1 - cdf_normal(1.11, 0, 1)))

# 5. P(Z < -0.66)
print("5. Result = %.4f" % (1 - cdf_normal(-0.66, 0, 1)))

# 6. P(0.28 < Z < 1.31)
print("6. Result = %.4f" % (cdf_normal(1.31, 0, 1) - cdf_normal(0.28, 0, 1)))

# 7. P(-0.86 < Z < 0.12)
print("7. Result = %.4f" % (cdf_normal(0.12, 0, 1) - cdf_normal(-0.86, 0, 1)))

# 8. P(-2.2 < Z < -0.16)
print("8. Result = %.4f" % (cdf_normal(-0.16, 0, 1) - cdf_normal(-2.2, 0, 1)))

# 9. X ~ N(20, 3^2)
print("9. Result = %.4f" % (cdf_normal(21, 20, 3) - cdf_normal(18, 20, 3)))

# 10. X ~ N(1.5, 0.1^2)
print("10. Result = %.4f" % (cdf_normal(0.5, 1.5, 0.1) - cdf_normal(-0.5, 1.5, 0.1)))
