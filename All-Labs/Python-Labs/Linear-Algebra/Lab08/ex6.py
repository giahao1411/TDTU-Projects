#bai 6

import numpy as np 
import sympy as sp
import matplotlib.pyplot as plt 

A = np.array([
    [1, 1, 1, 1],
    [8, 4, 2, 1],
    [27, 9, 3, 1],
    [4**3, 16, 4, 1],
    [5**3, 25, 5, 1],
    [6**3, 6**2, 6, 1]
])

b = np.array([2.1, 3.5, 4.2, 3.1, 4.4, 6.8]).T

res = np.linalg.lstsq(A, b, rcond = None)[0]

res1 = round(res[0], 5)
res2 = round(res[1], 5)
res3 = round(res[2], 5)
res4 = round(res[3], 5)

print("res[1] =", res1)
print("res[2] =", res2)
print("res[3] =", res3)
print("res[4] =", res4)

y = lambda x: res1*x**3 + res2*x**2 + res3*x + res4

x_arr = np.arange(0, 6.1, 0.1)
y_arr = list(map(y, x_arr))

plt.scatter([1, 2, 3, 4, 5, 6], b)
plt.plot(x_arr, y_arr)
plt.title("Exercise 6")
plt.show()