import sympy as sp 
import math 

x = sp.symbols('x')

#5a 
fa = x**2 - 7
lim_a = sp.limit(fa, x, 1)
print("lim a = ", lim_a)

f5a = lambda x: x**2 - 7
print("fa(1) = ", f5a(1))

if lim_a == f5a(1):
    print("f(x) is continuous at c = 1")
else:
    print("f(x) is NOT continuous at c = 1")

#5b
fb = sp.sqrt(2*x - 3)
lim_b = sp.limit(fb, x, 2)
print("lim b = ", lim_b)

f5b = lambda x: sp.sqrt(2*x - 7)
print("fb(2) = ", f5b(2))

if lim_b == f5b(2):
    print("f(x) is continuous at c = 2")
else:
    print("f(x) is NOT continuous at c = 2")