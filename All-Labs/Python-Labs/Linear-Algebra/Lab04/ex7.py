#bai 7

import sympy as sp

child, adult = sp.symbols('child, adult')

eq1 = sp.Eq(3*child + 3.2*adult, 118.4)
eq2 = sp.Eq(3.5*child + 3.6*adult, 135.2)

solve = sp.solve((eq1, eq2), (child, adult))
print(solve)