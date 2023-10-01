import sympy as sp
import math 

x = sp.symbols('x')

#1a
fa = abs(x**2 - x - 7)
lim_a = sp.limit(fa, x, 3)
print("1a - limit of fa(x) at x = 3 is: " + str(lim_a))

#1b
fb = (abs(x - 1))/(x**2 - 1)
lim_b = sp.limit(fb, x, 1)
print("1b - limit of fb(x) at x = 1 is: " + str(lim_b))

#1c 
fc = math.e**(1/x)
lim_c = sp.limit(fc, x, 1)
print("1c - limit of fc(x) at x = 1 is: " + str(lim_c))

#1d 
fd = (x**4 - 16)/(x - 2)
lim_d = sp.limit(fd, x, 2)
print("1d - limit of fd(x) at x = 2 is: " + str(lim_d))

#1e 
fe = (x**3 - x**2 - 5*x - 3)/((x + 1)**2)
lim_e = sp.limit(fe, x, -1)
print("1e - limit of fe(x) at x = -1 is: " + str(lim_e))

#1f
ff = (x**2 - 9)/((x**2 + 7)**(1/2) - 4)
lim_f = sp.limit(ff, x, 3)
print("1f - limit of ff(x) at x = 3 is: " + str(lim_f))

#1g
fg = (abs(x))/(sp.sin(x))
lim_g = sp.limit(fg, x, 1)
print("1g - limit of fg(x) at x = 1 is: " + str(lim_g))

#1h 
fh = (1 - sp.cos(x))/(x*sp.sin(x))
lim_h = sp.limit(fh, x, 0)
print("1h - limit of fh(x) at x = 0 is: " + str(lim_h))

#1i
fi = (2*x**2)/(3 - 3*sp.cos(x))
lim_i = sp.limit(fi, x, 0)
print("1i - limit of fi(x) at x = 0 is: " + str(lim_i))

#1j
fj = ((3 + x)/(x - 1))**x
lim_j = sp.limit(fj, x, sp.oo)
print("1j - limit of fj(x) at x = oo is: " + str(lim_j))

#1k
fk = (1 - 2/(3 + x))**x
lim_k = sp.limit(fk ,x, sp.oo)
print("1k - limit of fk(x) at x = oo is: " + str(lim_k))

#1l
fl = (1/x)**(1/x)
lim_l = sp.limit(fl, x, sp.oo)
print("1l - limit of fl(x) at x = oo is: " + str(lim_l))

#1m
fm = (-x**(1/3 + (1 + x)**(1/3)))/(-x**(1/2) + (1 + x)**(1/2))
lim_m = sp.limit(fm, x, sp.oo)
print("1m - limit of fm(x) at x = oo is: " + str(lim_m))

#1n
fn = (sp.factorial(x))/(x**x)
lim_n = sp.limit(fn, x, sp.oo)
print("1n - limit of fn(x) at x = 1 is: " + str(lim_n))




