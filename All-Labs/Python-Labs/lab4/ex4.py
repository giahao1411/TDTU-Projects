import sympy as sp 
import math

x = sp.symbols('x')

limL = 0

fxR = sp.sin(1/x)
limR = sp.limit(fxR, x, 0, '+')
print("limR = ", limR)

print("limL = lim 0 = 0")

if limR == limL:
    print("lim = limL = limR = ", limL)
else:
    print("lim # limL # limR. So lim does NOT exist")
    
    
