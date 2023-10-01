import sympy as sp 
import numpy as np 

x,m = sp.symbols('x, m')

y = x**3 - 3*m*x**2 + 3*(m**2 - 1)*x - (m**2 - 1)

x0 = 1

print('y = ', y)

dy = y.diff(x)
print("y'= ", dy)

d2y = y.diff(x, 2)
print("y'' = ", d2y)

dy_x0 = dy.subs(x, x0)
print("y'(x0) = ", dy_x0)

d2y_x0 = d2y.subs(x, x0)
print("y''(x0) = ", d2y_x0)

ms = sp.solve(dy_x0)
print(ms)

list_d2y_x0 = [d2y_x0.subs(m, it).evalf() for it in ms]
print(list_d2y_x0)

result = [it for it in ms if d2y_x0.subs(m, it).evalf() < 0]
print(result)
