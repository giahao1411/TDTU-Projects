#bai 5

import numpy as np
import sympy as sp 

#cach 1:

x, y, z = sp.symbols('x, y, z')

eq1 = sp.Eq(x + 2*y + z, 1)
eq2 = sp.Eq(2*x + 2*y + 2*z, 1)
eq3 = sp.Eq(2*x + 4*y + z, 2)

sol = sp.solve((eq1, eq2, eq3), (x, y, z))
print("cach 1:\n", sol)

#cach 2:

A = np.array([
    [1, 2, 1],
    [2, 2, 2],
    [2, 4, 1]
])

b = np.array([[1], [1], [2]])

sol1 = np.linalg.solve(A, b)
print("cach 2:\n", sol1)

#cach 3 - su dung cong thuc tuyen tinh - invert A * b 

#tim ma tran nghich dao cua ma tran A bang - np.linalg.inv()
A_inv = np.linalg.inv(A)

sol2 = np.matmul(A_inv, b)

print("cach 3:\n", sol2)