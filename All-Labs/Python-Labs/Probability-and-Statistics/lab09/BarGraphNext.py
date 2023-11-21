import numpy as np
import matplotlib.pyplot as plt

data = [[30, 25, 50, 20], [40, 23, 51, 17]]

X = np.arange(4)

fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
ax.bar(X + 0.00, data[0], color="b", width=0.25)
ax.bar(X + 0.25, data[1], color="g", width=0.25)
ax.set_xticks([0.25, 1.25, 2.25, 3.25])
ax.set_xticklabels([2015, 2016, 2017, 2018])
ax.legend(labels=["Oranges", "Apples"])
plt.show()
