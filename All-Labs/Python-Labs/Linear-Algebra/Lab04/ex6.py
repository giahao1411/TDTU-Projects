#bai 6 

import sympy as sp

a0, a1, a2 = sp.symbols('a0, a1, a2')

eq1 = sp.Eq(a0 + a1 + a2, 6)              #t = 1, pt = 6
eq2 = sp.Eq(a0 + a1*2 + a2*2**2, 15)      #t = 2, pt = 15
eq3 = sp.Eq(a0 + a1*3 + a1*3**2, 38)      #t = 3, pt = 38 

solve = sp.solve((eq1, eq2, eq3), (a0, a1, a2))
print(solve)