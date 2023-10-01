import sympy as sp

t = sp.symbols('t')

v = 160 - 32*t

v_in = sp.integrate(v, (t, 0, 8))
print("Definite integral of v from 0 to 8 = ", v_in.evalf(), "ft")