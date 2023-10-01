import sympy as sp 
import math

x = sp.symbols('x')

#3.1
print("3.1")

f3_1 = 1/(1 + 2**(1/x))

limR1 = sp.limit(f3_1, x, 0, '+')
print("limR = ", limR1)

limL1 = sp.limit(f3_1, x, 0, '-')
print("limL = ", limL1)

if limR1 == limL1:
    print("lim1 = limR1 = limL1 = ", limR1)
else:
    print("lim1 # limR1 # limL1")

#3.2 
print("3.2")

f3_2 = (x**2 + x)/(sp.sqrt((x**3 + x**2)))

limR2 = sp.limit(f3_2, x, 0, '+')
print("limR2 = ", limR2)

limL2 = sp.limit(f3_2, x, 0, '-')
print("limL2 = ", limL2)

if limR2 == limL2:
    print("lim2 = limR2 = limL2 = ", limL2)
else:
    print("lim2 # limR2 # limL2")



