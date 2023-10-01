import sympy as sp 

x, y = sp.symbols('x, y')

fa = y**2*x**4*sp.exp(x) + 2 

print(sp.diff(sp.diff(fa, y, 3), x, 2))

fb = y**4 + y*(sp.sin(x) - x**4)

print(sp.diff(sp.diff(fb, y, 3), x, 2))

fc = x**5 + 5*x*y + sp.sin(x) + 7*sp.exp(x)

print(sp.diff(sp.diff(fc, y, 3), x, 2))

fd = x*sp.exp((y**4)/2)

print(sp.diff(sp.diff(fd, y, 3), x, 2))

