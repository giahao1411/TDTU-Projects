import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from sympy import *

x = sp.symbols('x')

fa = lambda x: 1 - x
fb = lambda x: x**2 + 1
fc = lambda x: cos(x)
fd = lambda x: abs(x)

#a
x0a = np.arange(0, 1.1, 0.1)
y0a = list(map(fa, x0a))

plt.title("fa")
plt.plot(x0a, y0a)
plt.grid()
plt.show()

#b
x0b = np.arange(0, 1.1, 0.1)
y0b = list(map(fb, x0b))

plt.title("fb")
plt.plot(x0b, y0b)
plt.grid()
plt.show()

#c
x0c = np.arange(-pi, pi, pi)
y0c = list(map(fc, x0c))

plt.title("fc")
plt.plot(x0c, y0c)
plt.grid()
plt.show()

#d
x0d = np.arange(-1, 1.1, 0.1)
y0d = list(map(fd, x0d))

plt.title("fd")
plt.plot(x0d, y0d)
plt.grid()
plt.show()

