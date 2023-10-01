#bai 5

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

A = np.array([
    [np.cos(1), np.sin(1)],
    [np.cos(2), np.sin(2)],
    [np.cos(3), np.sin(3)]
])

b = np.array([7.9, 5.4, -9])

res = np.linalg.lstsq(A, b, rcond = None)[0]

print("res = ", res)

x1 = res[0]
x2 = res[1]

print("- x1 =", round(x1, 1))
print("- x2 =", round(x2, 1))

#initiate symbol x and define a function called y
x = sp.symbols('x')
y = lambda x: 7.9*np.cos(x) + 6.9*np.sin(x)

x_arr = np.arange(0, 6.1, 0.1)
y_arr = list(map(y, x_arr))

plt.scatter([1, 2, 3], b)
plt.plot(x_arr, y_arr, color = "red")
plt.title("Exercise 5")
plt.grid()