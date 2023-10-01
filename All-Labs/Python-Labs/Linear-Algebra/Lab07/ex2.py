#bai 2

import numpy as np
import sympy as sp

#cau a
v1a = np.array([1, -2, 0])
v2a = np.array([0, -4, 1])
v3a = np.array([1, -1, 1])

Aa = np.array([v1a, v2a, v3a]).T

rank_a = np.linalg.matrix_rank(Aa)

if rank_a == len([v1a, v2a, v3a]):
  print("a. is independent")
else:
  print("a. is dependent")

#cau b
v1b = np.array([1, 0, 2])
v2b = np.array([0, 1, 4])
v3b = np.array([2, -2, -4])

Ab = np.array([v1b, v2b, v3b]).T

rank_b = np.linalg.matrix_rank(Ab)

if rank_b == len([v1b, v2b, v3b]):
  print("b. is independent")
else:
  print("b. is dependent")

#khoi tao a, b, c
a, b, c = sp.symbols('a, b, c')

eq1 = sp.Eq(1*a + 2*c, 0)
eq2 = sp.Eq(1*b - 2*c, 0)
eq3 = sp.Eq(2*a + 4*b -4*c, 0)

sol = sp.solve((eq1, eq2, eq3), (a, b, c))
print(sol)

#cau c
v1c = np.array([1, -2, 3, 4])
v2c = np.array([2, 4, 5, 0])
v3c = np.array([-2, 0, 0, 4])
v4c = np.array([3, 2, 1, -1])

Ac = np.array([v1c, v2c, v3c, v4c])

rank_c = np.linalg.matrix_rank(Ac)

if rank_c == len([v1c, v2c, v3c, v4c]):
  print("c. is independent")
else:
  print("c. is dependent")

#cau d
v1d = np.array([0, 0, 1, 2, 3])
v2d = np.array([0, 0, 2, 3, 1])
v3d = np.array([1, 2, 3, 4, 5])
v4d = np.array([2, 1, 0, 0, 0])
v5d = np.array([-1, -3, -5, 0, 0])

Ad = np.array([v1d, v2d, v3d, v4d, v5d])

rank_d = np.linalg.matrix_rank(Ad)

if rank_d == len([v1d, v2d, v3d, v4d, v5d]):
  print("d. is independent")
else:
  print("d. is dependent")