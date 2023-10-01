import numpy as np
import matplotlib.pyplot as plt

f1 = lambda x: (1 - (abs(x) - 1)**2)**(1/2)
f2 = lambda x: -3 * (1 - (abs(x)/2)**(1/2))**(1/2)

x = np.arange(-2, 2.1, 0.001)

y1 = list(map(f1, x))

plt.plot(x, y1, color = 'magenta')

y2 = list(map(f2, x))

plt.plot(x, y2, color = 'red')
plt.grid()
plt.show()