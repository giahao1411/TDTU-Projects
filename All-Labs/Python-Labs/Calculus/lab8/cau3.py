import sympy as sp 

x, y = sp.symbols('x, y')

fa = 2*x*2 - 3*y - 4

dfx_a = sp.diff(fa, x)
dfy_a = sp.diff(fa, y)

print("first order partial derivative of f(x,y) with regard to x = ", dfx_a)
print("first order partial derivative of f(x,y) with regard to y = ", dfy_a)

fb = (x**2 - 1)*(y + 2)

dfx_b = sp.diff(fb, x)
dfy_b = sp.diff(fb, y)

print("first order partial derivative of f(x,y) with regard to x = ", dfx_b)
print("first order partial derivative of f(x,y) with regard to y = ", dfy_b)

fc = x**2 - x*y + y**2

dfx_c = sp.diff(fc, x)
dfy_c = sp.diff(fc, y)

print("first order partial derivative of f(x,y) with regard to x = ", dfx_c)
print("first order partial derivative of f(x,y) with regard to y = ", dfy_c)

fd = 5*x*y - 7*x**2 - y**2 + 3*x - 6*y + 2 

dfx_d = sp.diff(fd, x)
dfy_d = sp.diff(fd, y)

print("first order partial derivative of f(x,y) with regard to x = ", dfx_d)
print("first order partial derivative of f(x,y) with regard to y = ", dfy_d)

fe = (x*y - 1)**2 

dfx_e = sp.diff(fe, x)
dfy_e = sp.diff(fe, y)

print("first order partial derivative of f(x,y) with regard to x = ", dfx_e)
print("first order partial derivative of f(x,y) with regard to y = ", dfy_e)

ff = (2*x - 3*y)**3

dfx_f = sp.diff(ff, x)
dfy_f = sp.diff(ff, y)

print("first order partial derivative of f(x,y) with regard to x = ", dfx_f)
print("first order partial derivative of f(x,y) with regard to y = ", dfy_f)

fg = (x**2 + y**2)**(1/2)

dfx_g = sp.diff(fg, x)
dfy_g = sp.diff(fg, y)

print("first order partial derivative of f(x,y) with regard to x = ", dfx_g)
print("first order partial derivative of f(x,y) with regard to y = ", dfy_g)

fh = (x**3 + y/2)**(2/3)

dfx_h = sp.diff(fh, x)
dfy_h = sp.diff(fh, y)

print("first order partial derivative of f(x,y) with regard to x = ", dfx_h)
print("first order partial derivative of f(x,y) with regard to y = ", dfy_h)

fi = 1/(x + y)

dfx_i = sp.diff(fi, x)
dfy_i = sp.diff(fi, y)

print("first order partial derivative of f(x,y) with regard to x = ", dfx_i)
print("first order partial derivative of f(x,y) with regard to y = ", dfy_i)

fj = x/(x**2 + y**2)

dfx_j = sp.diff(fj, x)
dfy_j = sp.diff(fj, y)

print("first order partial derivative of f(x,y) with regard to x = ", dfx_j)
print("first order partial derivative of f(x,y) with regard to y = ", dfy_j)

fk = (x + y)/(x*y - 1)

dfx_k = sp.diff(fk, x)
dfy_k = sp.diff(fk, y)

print("first order partial derivative of f(x,y) with regard to x = ", dfx_k)
print("first order partial derivative of f(x,y) with regard to y = ", dfy_k)

fl = 1/sp.tan(y/x)

dfx_l = sp.diff(fl, x)
dfy_l = sp.diff(fl, y)

print("first order partial derivative of f(x,y) with regard to x = ", dfx_l)
print("first order partial derivative of f(x,y) with regard to y = ", dfy_l)

fm = sp.exp(x + y + 1)

dfx_m = sp.diff(fm, x)
dfy_m = sp.diff(fm, y)

print("first order partial derivative of f(x,y) with regard to x = ", dfx_m)
print("first order partial derivative of f(x,y) with regard to y = ", dfy_m)

fn = sp.exp(-x)*sp.sin(x + y)

dfx_n = sp.diff(fn, x)
dfy_n = sp.diff(fn, y)

print("first order partial derivative of f(x,y) with regard to x = ", dfx_n)
print("first order partial derivative of f(x,y) with regard to y = ", dfy_n)

fo = sp.log(x + y)

dfx_o = sp.diff(fo, x)
dfy_o = sp.diff(fo, y)

print("first order partial derivative of f(x,y) with regard to x = ", dfx_o)
print("first order partial derivative of f(x,y) with regard to y = ", dfy_o)