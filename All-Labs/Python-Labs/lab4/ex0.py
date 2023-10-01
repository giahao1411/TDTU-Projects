import sympy as sp 
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-10, 10.1, 0.1)

f1 = lambda x: -x + 5
f2 = lambda x: x/2 + 2

y1 = list(map(f1, x))
y2 = list(map(f2, x))

plt.plot(x, y1)
plt.plot(x, y2)

x = sp.symbols('x')
f1 = -x + 5
f2 = x/2 + 2 

x_root = sp.solve((-3/2)*x + 3)
y_root = f1.subs(x, x_root[0])

plt.plot(x_root, y_root, 'ro')
plt.title('Find intersection point of f1(x) and f2(x)')
plt.grid(linestyle = '--')
plt.show()