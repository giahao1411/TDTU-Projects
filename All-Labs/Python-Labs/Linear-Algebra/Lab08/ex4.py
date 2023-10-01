#bai 4 - ve nha lam

import numpy as np
import sympy as sp 
import matplotlib.pyplot as plt

A = np.array([
    [1, 2000],
    [1, 6000],
    [1, 20000],
    [1, 30000],
    [1, 40000]
])

b = np.array([20, 18, 10, 6, 2]).T

res = np.linalg.lstsq(A, b, rcond = None)[0]

print("res =", res)

x1 = round(res[0], 1)
x2 = round(res[1], 1)

print("- x1 =", x1, "\n- x2 =", x2)

#initiate symbol x and define function called y
x = sp.symbols('x')
y = lambda x: 20.6*x 

x_arr = np.arange(0 ,50000, 2000)
y_arr = list(map(y, x_arr))

plt.scatter([2000, 6000, 20000, 30000, 40000], b)
plt.plot(x_arr, y_arr, color = "pink")
plt.title("Exercise 4")
plt.show()