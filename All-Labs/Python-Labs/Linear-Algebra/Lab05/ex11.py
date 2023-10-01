#bai 11

import sympy as sp
from sympy.solvers.solveset import linsolve

#cach 1

x1, x2, x3, x4 = sp.symbols('x1, x2, x3, x4')

eq1 = sp.Eq(3*x1 - x3, 0)
eq2 = sp.Eq(8*x1 - 2*x4, 0)
eq3 = sp.Eq(2*x2 - 2*x3, 0)

sol = sp.solve((eq1, eq2, eq3), (x1, x2, x3, x4))

print(sol)

#cach 2
X = linsolve([3*x1 - x3, 8*x1 - 2*x4, 2*x2 - 2*x3 - x4], (x1, x2, x3, x4))
print("X = ",X)
print("(x1)C3H8 + (x2)O2 −→ (x3)CO2 + (x4)H2O")