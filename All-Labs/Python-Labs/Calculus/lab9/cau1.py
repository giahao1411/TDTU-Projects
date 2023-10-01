import sympy as sp 

x = sp.symbols('x')

fa = 3*x**4 - 16*x**3 + 18*x**2 - 9
dfa = sp.diff(fa, x)
print("Critical values: ", sp.solve(dfa, x))

fb = (x + 2)/(2*x**2)
dfb = sp.diff(fb, x)
print("Critical values: ", sp.solve(dfb, x))

fc = -(x**2)/3 + x**2 + 3*x + 4
dfc = sp.diff(fc, x)
print("Critical values: ", sp.solve(dfc, x))

fd = (5*x**2 + 5)/x
dfd = sp.diff(fd, x)
print("Critical values: ", sp.solve(dfd, x))

