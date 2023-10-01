import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from sympy import *

x = sp.symbols('x')

#a
fa = lambda x: x**2*cos(x)

x0a = np.arange(-4, 9.1, 0.1)
y0a = list(map(fa, x0a))

plt.plot(x0a, y0a)
plt.grid()
plt.show()

f_abs = abs(x**2*cos(x))

f_abs_in = sp.integrate(f_abs, (x, -4, 9))
print("Area bounded between f(x) and x-axis = ", f_abs_in.evalf())

#b
fb = lambda x: exp(-x**2/2)

x0b = np.arange(-10, 10.1, 0.1)
y0b = list(map(fb, x0b))

plt.plot(x0b, y0b)
plt.grid()
plt.show()

fb_abs = abs(exp(-x**2/2))

fb_abs_in = sp.integrate(fb_abs, (x, -oo, oo))
print("Area bounded between f(x) and x-axis = ", fb_abs_in.evalf())