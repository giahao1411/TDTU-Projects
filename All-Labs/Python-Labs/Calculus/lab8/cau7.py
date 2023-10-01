import sympy as sp 
import math

t = sp.symbols('t')

#a
print("Cau a")
xa = sp.cos(t)
ya = sp.sin(t)
wa = xa**2 + ya**2

dwt_a = sp.diff(wa, t)
print("Derivative of w(t) with regard to t = ", dwt_a)
print("Derivative of w(t) with regard to t at t = pi: ", dwt_a.subs(t, math.pi))
print(ya.subs(t, 3).evalf())

#b
print("Cau b")
xb = sp.cos(t) + sp.sin(t)
yb = sp.cos(t) - sp.sin(t)
wb = xb**2 + yb**2

dwt_b = sp.diff(wb, t)
print("Derivative of w(t) with regard to t = ", dwt_b)
print("Derivative of w(t) with regard to t at t = 0: ", dwt_b.subs(t, 0))
print(yb.subs(t, 3).evalf())

#c 
print("Cau c")
xc = sp.cos(t)**2 
yc = sp.sin(t)**2
zc = 1/t 
wc = xc/zc + yc/zc

dwt_c = sp.diff(wc, t)
print("Derivative of w(t) with regard to t = ", dwt_c)
print("Derivative of w(t) with regard to t at t = 3: ", dwt_c.subs(t, 3))
print(yc.subs(t, 3).evalf())

#d
print("Cau d")
xd = sp.log(t**2 + 1)
yd = 1/sp.tan(t)
zd = sp.exp(t)
wd = 2*yd*sp.exp(xd) - sp.log(zd)

dwt_d = sp.diff(wd, t)
print("Derivative of w(t) with regard to t = ", dwt_d)
print("Derivative of w(t) with regard to t at t = 1: ", dwt_d.subs(t, 1))
print(yd.subs(t, 3).evalf())

#e 
print("Cau e")
xe = t 
ye = sp.log(t)
ze = sp.exp(t - 1) 
we = ze - sp.sin(xe*ye)

dwt_e = sp.diff(we, t)
print("Derivative of w(t) with regard to t = ", dwt_e)
print("Derivative of w(t) with regard to t at t = 1: ", dwt_e.subs(t, 1))
print(ye.subs(t, 3).evalf())