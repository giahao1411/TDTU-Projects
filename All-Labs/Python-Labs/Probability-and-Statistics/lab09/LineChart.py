import numpy as np
import matplotlib.pyplot as plt

samples = [0.895, 0.91, 0.919, 0.926, 0.929, 0.931]
plt.plot(samples)
plt.show()
# we can add the x-axis values
years = [2010, 2011, 2012, 2013, 2014, 2015]
plt.plot(years, samples)

plt.xlabel("Year")
plt.ylabel("Yeild")
plt.plot(years, samples)
plt.show()
