import matplotlib.pyplot as plt
import numpy as np
import math

i = lambda x: -x**3 

x = np.arange(-100, 101, 1)

yi = list(map(i, x))

plt.plot(x, yi)
plt.grid()
plt.show()

j = lambda x: -1/(x**2)

yj = list(map(j, x))

plt.plot(x, yj)
plt.grid()
plt.show()

k = lambda x: -1/x

yk = list(map(k, x))

plt.plot(x, yk)
plt.grid()
plt.show()

l = lambda x: 1/abs(x)

yl = list(map(l, x))

plt.plot(x, yl)
plt.grid()
plt.show()

m = lambda x: (abs(x))**(1/2)

ym = list(map(m, x))

plt.plot(x, ym)
plt.grid()
plt.show()

n = lambda x: (abs(-x))**(1/2)

yn = list(map(n, x))

plt.plot(x, yn)
plt.grid()
plt.show()