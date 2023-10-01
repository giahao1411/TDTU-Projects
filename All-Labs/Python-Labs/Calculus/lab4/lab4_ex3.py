import sympy as sp

x = sp.symbols('x')

fx1 = 1/(1 + 2**(1/x))
fx2 = (x**2 + x)/((x**3 + x**2)**(1/2))

limR1 = sp.limit(fx1, x, 0, '+')
print("LimR = ", limR1)

limL1 = sp.limit(fx1, x, 0, '-')
print("LimL = ", limL1)

if limR1 == limL1:
    print("lim_fx1 is exist and lim_fx1 = ", limL1)
else:
    print("lim_fx1 is NOT exist!")

limR2 = sp.limit(fx2, x, 0, '+')
print("LimR = ", limR2)

limL2 = sp.limit(fx2, x, 0, '-')
print("LimL = ", limL2)

if limR2 == limL2:
    print("lim_fx2 is exist and lim_fx2 = ", limL2)
else:
    print("lim_fx2 is NOT exist!")
