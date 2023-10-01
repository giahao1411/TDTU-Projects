#bai 3

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

#-----------cau a-----------
print("-----Cau a:-----")
A = np.array([
    [1, 0],
    [1, 1],
    [1, 2],
    [1, 3]
])

b = np.array([1, 1, 2, 2]).T

sol = np.linalg.lstsq(A, b, rcond = None)

print("sol =", sol)

x = sol[0]

print("- x[1] = ", round(x[0], 1))
print("- x[2] = ", x[1])

#initiate symbol x
x = sp.symbols('x')

y = lambda x: 0.9 + 0.4*x

x_arr = np.arange(0, 6.1, 0.1)
y_arr = list(map(y, x_arr))

#plot 
plt.scatter([0, 1, 2, 3], b, color = "blue", label = "data point")
plt.title("----Cau a----")
plt.plot(x_arr, y_arr, "r", label = "least squares line")
plt.show()

#-----------cau b-----------
print("-----Cau b:-----")
A1 = np.array([
    [1, 1],
    [1, 2],
    [1, 4],
    [1, 5]
])

b1 = np.array([0, 1, 2, 3]).T 

res = np.linalg.lstsq(A1, b1, rcond = None)

print("res = ", res)

x1 = res[0]

print("- x[1] = ", round(x1[0], 5), "\n- x[2] = ", round(x1[1], 5))


y1 = lambda x: -0.6 + 0.7*x

x1_arr = np.arange(0, 6.1, 0.1)
y1_arr = list(map(y1, x1_arr))

plt.scatter([1, 2, 4, 5], b1, color = "red", label = "data point")
plt.title("----Cau b----")
plt.plot(x1_arr, y1_arr, "r", label = "least squares line")
plt.show()

#-----------cau c-----------
print("-----Cau c-----")

A2 = np.array([
    [1, -1],
    [1, 0],
    [1, 1],
    [1, 2]
])