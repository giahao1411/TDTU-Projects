import sympy as sp

x = sp.symbols('x')

#a 
fa = x**2 - 1

fa_in = sp.integrate(fa, (x, 0, 3**(1/2)))
print("Average value = ", 1/(3**(1/2) - 0)*fa_in.evalf())

#b
fb = -x**2/2

fb_in = sp.integrate(fb, (x, 0, 3))
print("Average value = ", 1/3*fb_in.evalf())

#c
fc = -3*x**2 - 1

fc_in = sp.integrate(fc, (x, 0, 1))
print("Average value = ", fc_in.evalf())

#d
fd = x**2 - x

fd_in = sp.integrate(fd, (x, -2, 1))
print("Average value = ", 1/3*fd_in.evalf())