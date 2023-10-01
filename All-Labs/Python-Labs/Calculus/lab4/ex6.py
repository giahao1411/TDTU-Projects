import sympy as sp
import numpy as np

x = sp.symbols('x')

#cau a:
print("Cau 6a:")
fa = (x**2 - x - 6)/(x - 3)

#at time x=0:
lim_x_0a = sp.limit(fa, x, 0)

print("f(x) is continuous for all x#: ")

if lim_x_0a != 5:
    print(0)

#at time x!=0:
for a in np.arange(-100, 100, 1):
    if a!= 0:
        lim_x_a = sp.limit(fa, x, a)
        fa_a = fa.subs(x, a)
        if lim_x_a != fa_a:
            print(a)

#cau b:
print("Cau 6b:")
fb = (x**3 - 8)/(x**2 - 4)

#at time x=2:
lim_x_p2b = sp.limit(fb, x, 2) #p:plus

print("f(x) is continuous for all x#: ")

if lim_x_p2b != 3:
    print(2)

#at time x=-2:
lim_x_m2b = sp.limit(fb, x, -2) #m:minus

if lim_x_m2b != 4:
    print(-2)

#at time x!=2 && x!=-2:
for b in np.arange(-100, 100, 1):
    if(b!=2 and b!=-2):
        lim_x_b = sp.limit(fb, x, b)
        fb_b = fb.subs(x, b)
        if lim_x_b != fb_b:
            print(b)

#cau c:
print("Cau 6c:")
fc = (x**2 - x - 2)/(x - 2)

#at time x=2:
lim_x_2c = sp.limit(fc, x, 2)

print("f(x) is continuous for all x#: ")

if lim_x_2c != 1:
    print(2)

#at time x!=0:
for c in np.arange(-100, 100, 1):
    if c!= 2:
        lim_x_c = sp.limit(fc, x, c)
        fc_c = fc.subs(x, c)
        if lim_x_c != fc_c:
            print(c)

#cau d:
print("Cau 6d:")
fd = 1/(x**2)

#at time x=0:
lim_x_0d = sp.limit(fd, x, 0)

print("f(x) is continuous for all x#: ")

if lim_x_0d != 1:
    print(0)

#at time x!=0:
for d in np.arange(-100, 100, 1):
    if d!= 0:
        lim_x_d = sp.limit(fd, x, d)
        fd_d = fd.subs(x, d)
        if lim_x_d != fd_d:
            print(d)
