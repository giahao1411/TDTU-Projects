#bai 20

import sympy as sp

c1, c2, c3, c4 = sp.symbols('c1, c2, c3, c4')

eq1 = sp.Eq(c1 + c2 + c3 + c4, 1000)
eq2 = sp.Eq(c1 + 2*c2 + 2**2*c3 + 2**3*c4, 2000)
eq3 = sp.Eq(c1 + 3*c2 + 3**2*c3 + 3**3*c4, 3000)
eq4 = sp.Eq(c1 + 4*c2 + 4**2*c3 + 4**3*c4, 4000)

sol = sp.solve((eq1, eq2, eq3, eq4), (c1, c2, c3, c4))

print(sol)