import numpy as np
import matplotlib.pyplot as plt

years = range(2000, 2006)
oranges = [0.4, 0.8, 0.9, 0.7, 0.6, 0.8]

plt.xlabel("Year")
plt.ylabel("Yeild")
plt.bar(years, oranges)
plt.show()

apples = [0.35, 0.6, 0.9, 0.8, 0.65, 0.8]
plt.bar(years, apples)
plt.bar(years, oranges, bottom=apples)
plt.show()