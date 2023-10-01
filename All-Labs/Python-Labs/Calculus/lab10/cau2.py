import sympy as sp

x, y = sp.symbols('x, y')

#a
fa = x**3 - 3*sp.sin(x)*sp.cos(x)

fa_in = sp.integrate(fa, (x, 0, sp.pi/2))
print("Definite integral of fa from 0 to pi/2 = ", fa_in.evalf())

#b
print("---------------")
fb = (sp.sin(x**2)**2)

fb_in = sp.integrate(fb, (x, 0, 1))
print("Definite integral of fb from 0 to 1 = ", fb_in.evalf())

#c
print("---------------")
fc = (1 + (x**2 + 1) + (x + 1)**2)**(1/2)

fc_in = sp.integrate(fc, (x, 0, 3))
print("Definite integral of fc from 0 to 3 = ", fc_in.evalf())

#d
print("---------------")
fd = x**2*y

fd_in = sp.integrate(fd, (x, 0, 3), (y, 1, 2))
print("Definite integral of fd = ", fd_in.evalf())