import sympy as sp

x, y = sp.symbols('x, y')

fa = x + y + x*y 

print("second order partial derivative of f(x,y) with regard to x = ", sp.diff(fa, x, 2))
print("second order partial derivative of f(x,y) with regard to y = ", sp.diff(fa, y, 2))

fb = sp.sin(x*y)

print("second order partial derivative of f(x,y) with regard to x = ", sp.diff(fb, x, 2))
print("second order partial derivative of f(x,y) with regard to y = ", sp.diff(fb, y, 2))

fc = x**2*y + sp.cos(y) + y*sp.sin(x)

print("second order partial derivative of f(x,y) with regard to x = ", sp.diff(fc, x, 2))
print("second order partial derivative of f(x,y) with regard to y = ", sp.diff(fc, y, 2))

fd = x*sp.exp(y) + y + 1

print("second order partial derivative of f(x,y) with regard to x = ", sp.diff(fd, x, 2))
print("second order partial derivative of f(x,y) with regard to y = ", sp.diff(fd, y, 2))

fe = sp.log(x + y)

print("second order partial derivative of f(x,y) with regard to x = ", sp.diff(fe, x, 2))
print("second order partial derivative of f(x,y) with regard to y = ", sp.diff(fe, y, 2))

ff = 1/sp.tan(y/x)

print("second order partial derivative of f(x,y) with regard to x = ", sp.diff(ff, x, 2))
print("second order partial derivative of f(x,y) with regard to y = ", sp.diff(ff, y, 2))

fg = x**2*sp.tan(x*y)

print("second order partial derivative of f(x,y) with regard to x = ", sp.diff(fg, x, 2))
print("second order partial derivative of f(x,y) with regard to y = ", sp.diff(fg, y, 2))

fh = y*sp.exp(x**2 - y)

print("second order partial derivative of f(x,y) with regard to x = ", sp.diff(fh, x, 2))
print("second order partial derivative of f(x,y) with regard to y = ", sp.diff(fh, y, 2))

fi = x*sp.sin(x**2*y)

print("second order partial derivative of f(x,y) with regard to x = ", sp.diff(fi, x, 2))
print("second order partial derivative of f(x,y) with regard to y = ", sp.diff(fi, y, 2))

fj = (x - y)/(x**2 + y)

print("second order partial derivative of f(x,y) with regard to x = ", sp.diff(fj, x, 2))
print("second order partial derivative of f(x,y) with regard to y = ", sp.diff(fj, y, 2))



