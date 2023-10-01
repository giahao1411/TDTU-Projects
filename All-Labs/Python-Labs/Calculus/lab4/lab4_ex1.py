import sympy as sp
import math

x = sp.symbols('x')

fa = abs(x**2 - x -7)
lim_a = sp.limit(fa, x, 3)

fb = abs(x - 1)/(x**2 - 1)
lim_b = sp.limit(fb, x, 1)

fc = math.e**(1/x)
lim_c = sp.limit(fc, x, 1)

fd = (x**4 - 16)/(x - 2)
lim_d = sp.limit(fd, x, 2)

fe = (x**3 - x**2 - 5*x - 3)/((x + 1)**2)
lim_e = sp.limit(fe, x, -1)

ff = (x**2 - 9)/((x**2 - 7)**(1/2) - 4)
lim_f = sp.limit(fe, x, 3)

fg = abs(x)/sp.sin(x)
lim_g = sp.limit(fd, x, 1)

fh = (1 - sp.cos(x))/(x*sp.sin(x))
lim_h = sp.limit(fh, x, 0)

fi = 2*x**2/(3 - 3*sp.cos(x))
lim_i = sp.limit(fi, x, 0)

fj = ((3 + x)/(x - 1))**x
lim_j = sp.limit(fj, x, sp.oo)

fk = (1 - 2/(3 + x))**x
lim_k = sp.limit(fk, x, sp.oo)

fl = (1/x)**(1/x)
lim_l = sp.limit(fl, x, sp.oo)

fm = (-x**(1/3) + (1 + x)**(1/3))/(-x**(1/2) + (1 + x)**(1/2))
lim_m = sp.limit(fm, x, sp.oo)

fn = sp.factorial(x)/(x**x)
lim_n = sp.limit(fn, x, sp.oo)

print("1a - The limit of f(x) at x = 3: " + str(lim_a))
print("1b - The limit of f(x) at x = 1: " + str(lim_b))
print("1c - The limit of f(x) at x = 1: " + str(lim_c))
print("1d - The limit of f(x) at x = 2: " + str(lim_d))
print("1e - The limit of f(x) at x = -1: " + str(lim_e))
print("1f - The limit of f(x) at x = 3: " + str(lim_f))
print("1g - The limit of f(x) at x = 1: " + str(lim_g))
print("1h - The limit of f(x) at x = 0: " + str(lim_h))
print("1i - The limit of f(x) at x = 0: " + str(lim_i))
print("1j - The limit of f(x) at x = oo: " + str(lim_j))
print("1k - The limit of f(x) at x = oo: " + str(lim_k))
print("1m - The limit of f(x) at x = oo: " + str(lim_m))
print("1n - The limit of f(x) at x = oo: " + str(lim_n))


