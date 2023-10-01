import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x = sp.symbols('x')

#cau a:
print("Cau 10a:")

fx_a = (sp.sin(x))/x

lim_xa = sp.limit(fx_a, x, 0)
lim_xa_R = sp.limit(fx_a, x, 0, '+')
lim_xa_L = sp.limit(fx_a, x, 0, '-')

if lim_xa == lim_xa_L == lim_xa_R:
    print("L = ", lim_xa)
else:
    print("L is not exist")

#cau b:
print("Cau 10b:")

fx_b = (x**2 + x - 6)/(x**2 - 4)

lim_xb = sp.limit(fx_b, x, 2)
lim_xb_R = sp.limit(fx_b, x, 2, '+')
lim_xb_L = sp.limit(fx_b, x, 2, '-')

if lim_xb == lim_xb_L == lim_xb_R:
    print("L = ", lim_xb)
else:
    print("L is not exist")