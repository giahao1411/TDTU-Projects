#bai 1

import sympy as sp
import numpy as np

x, y, z, t = sp.symbols('x, y, z, t')

#cau a
eq1 = sp.Eq(x + 2*y + z, 0)
eq2 = sp.Eq(2*x - y + z, 0)
eq3 = sp.Eq(2*x + y, 0)

sol1 = sp.solve((eq1, eq2, eq3), (x, y, z))
print("cau a: ", sol1)

#cau b
eq11 = sp.Eq(2*x + y + z + t, 1)
eq22 = sp.Eq(x + 2*y + z + t, 1)
eq33 = sp.Eq(x + y + 2*z + 2*t, 1)
eq44 = sp.Eq(x + y + z+ 2*t, 1)

sol2 = sp.solve((eq11, eq22, eq33, eq44), (x, y, z, t))
print("cau b: ", sol2)

#in kieu du lieu 
print(type(sol1), "\n")

#cach 2 - dua ve Ax = b: dung np.linalg.solve(A, b) -> tim x
A = np.array([
    [1, 2, 1],
    [2, -1, 1],
    [2, 1, 0]
])

b = np.array([
    [0],
    [0],
    [0]
])

x1 = np.linalg.solve(A, b)

print("cau a(cach 2): \n", x1)

B = np.array([
    [2, 1, 1, 1],
    [1, 2, 1, 1],
    [1, 1, 2, 2],
    [1, 1, 1, 2]
])

a = np.array([
    [1],
    [1],
    [1],
    [1]
])

y1 = np.linalg.solve(B, a)

print("cau b(cach 2): \n", y1)