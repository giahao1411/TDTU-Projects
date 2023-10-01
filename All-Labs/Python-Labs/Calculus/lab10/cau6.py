import sympy as sp

x = sp.symbols('x')

cdx = 1/(2*x**(1/2))

cdx_in = sp.integrate(cdx, (x, 1, 100))
print("c(100) - c(1) = ", cdx_in.evalf(), "dollars")