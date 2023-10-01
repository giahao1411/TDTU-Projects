import sympy as sp

x = sp.symbols('x')

#a 
fa = x**3 + 2*x**2 + 3 

fa_in = sp.integrate(fa, x)
print("Antiderivative of fa = ", fa_in)

fa_in12 = sp.integrate(fa, (x, 1, 2))
print("Definite integral of fa from 1 to 2 = ", fa_in12.evalf())

#b
print("---------------")
fb = 1/x**3 + 1/x**2 + x*x**(1/2)

fb_in = sp.integrate(fb, x)
print("Antiderivative of fb = ", fb_in)

fb_in14 = sp.integrate(fb, (x, 1, 4))
print("Definite integral of fb from 1 to 4 = ", fb_in14.evalf())

#c
print("---------------")
fc = (x**3 + x*x**(1/2) + x)/x**2

fc_in = sp.integrate(fc, x)
print("Antiderivative of fc = ", fc_in)

fc_in14 = sp.integrate(fc, (x, 1, 4))
print("Definite integral of fc from 1 to 4 = ", fc_in14.evalf())

#d
print("---------------")
fd = 2/x + x**3 

fd_in = sp.integrate(fd, x)
print("Antiderivative of fd = ", fd_in)

fd_in12 = sp.integrate(fd, (x, 1, 2))
print("Definite integral of fd from 1 to 2 = ", fd_in12.evalf())

#e
print("---------------")
fe = x**2*(1/x + 2*x)

fe_in = sp.integrate(fe, x)
print("Antiderivative of fe = ", fe_in)

fe_in12 = sp.integrate(fe, (x, 1, 2))
print("Definite integral of fe from 1 to 2 = ", fe_in12.evalf())

#f
print("---------------")
ff = (x**(1/2) - 1)*(x + x**(1/2) + 1)

ff_in = sp.integrate(ff, x)
print("Antiderivative of ff = ", ff_in)

ff_in01 = sp.integrate(ff, (x, 0, 1))
print("Definite integral of ff from 0 to 1 = ", ff_in01.evalf())

#g
print("---------------")
fg = (1 - 2/(sp.sin(x)**2))

fg_in = sp.integrate(fg, x)
print("Antiderivative of fg = ", fg_in)

fg_pi4_pi2 = sp.integrate(fg, (x, sp.pi/4, sp.pi/2))
print("Definite integral of fg from pi/4 to pi/2 = ", fg_pi4_pi2.evalf())

#h
print("---------------")
fh = 1/((sp.sin(x)**2)*(sp.cos(x)**2))

fh_in = sp.integrate(fh, x)
print("Antiderivative of fh = ", fh_in)

fh_in_pi6_pi4 = sp.integrate(fh, (x, sp.pi/6, sp.pi/4))
print("Definite integral of fh from pi/6 to pi/4 = ", fh_in_pi6_pi4.evalf())

#i
print("---------------")
fi = sp.exp(x)*(1 - sp.exp(-x)/(sp.cos(x)**2))

fi_in = sp.integrate(fi, x)
print("Antiderivative of fi = ", fi_in)

fi_in_0_pi4 = sp.integrate(fi, (x, 0, sp.pi/4))
print("Definite integral of fi from 0 to pi/4 = ", fi_in_0_pi4.evalf())
