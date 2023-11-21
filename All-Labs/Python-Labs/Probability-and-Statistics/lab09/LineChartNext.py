import matplotlib.pyplot as plt
import numpy as np

years = range(2000, 2012)
apples = [0.895, 0.91, 0.919, 0.926, 0.929, 0.931, 0.934, 0.936, 0.937, 0.9375, 0.932, 0.925]
oranges = [0.962, 0.941, 0.930, 0.923, 0.918, 0.908, 0.907, 0.904, 0.901, 0.898, 0.890, 0.885]

plt.plot(years, apples)
plt.plot(years, oranges)
plt.xlabel("Year")
plt.ylabel("Yeild")

plt.title("Crop Yields in Kanto")
plt.legend(['Apples', 'Oranges'])

plt.plot(years, apples, marker='x')
plt.plot(years, oranges, marker='o')
plt.show()

#show another figure
plt.figure(figsize=(9, 3))
plt.plot(years, apples, marker='x')
plt.show()