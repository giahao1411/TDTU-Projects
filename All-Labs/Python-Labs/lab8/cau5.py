import sympy as sp  

x, y = sp.symbols('x, y')

fa = x*sp.sin(y) + y*sp.sin(x) + x*y 

print(sp.diff(sp.diff(fa, x), y))
print(sp.diff(sp.diff(fa, y), x))

fb = sp.log(2*x + 3*y)

print(sp.diff(sp.diff(fb, x), y))
print(sp.diff(sp.diff(fb, y), x))

fc = x*y**2 + x**2*y**3 + x**3*y**4

print(sp.diff(sp.diff(fc, x), y))
print(sp.diff(sp.diff(fc, y), x))

fd = sp.exp(x) + x*sp.log(y) + y*sp.log(x)

print(sp.diff(sp.diff(fd, x), y))
print(sp.diff(sp.diff(fd, y), x))


