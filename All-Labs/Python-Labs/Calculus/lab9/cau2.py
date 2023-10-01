import sympy as sp 

x = sp.symbols('x')

#cau a -----------------------------------------
fa = 3*x**4 - 16*x**3 + 18*x**2 - 9

dfa = sp.diff(fa, x)
dfa2 = sp.diff(fa, x, 2)

print("Critical values:", sp.solve(dfa, x))

for i in sp.solve(dfa, x):
    if dfa2.subs(x, i) > 0:
        print("fa has a local minimum at", i)
    elif dfa2.subs(x, i) < 0:
        print("fa has a local maximum at", i)
    else:
        print("fa is not define")

#cau b -----------------------------------------
fb = (x + 2)/(2*x**2)

dfb = sp.diff(fb, x)
dfb2 = sp.diff(fb, x, 2)

print("Critical values:", sp.solve(dfb, x))

for i in sp.solve(dfb, x):
    if dfb2.subs(x, i) > 0:
        print("fb has a local minimum at", i)
    elif dfb2.subs(x, i) < 0:
        print("fb has a local maximum at", i)
    else:
        print("fb is not define")

#cau c -----------------------------------------
fc = -(x**2)/3 + x**2 + 3*x + 4

dfc = sp.diff(fc, x)
dfc2 = sp.diff(fc, x, 2)

print("Critical values:", sp.solve(dfc, x))

for i in sp.solve(dfc, x):
    if dfc2.subs(x, i) > 0:
        print("fc has a local minimum at", i)
    elif dfc2.subs(x, i) < 0:
        print("fc has a local maximum at", i)
    else:
        print("fc is not define")

#cau d -----------------------------------------
fd = (5*x**2 + 5)/x

dfd = sp.diff(fd, x)
dfd2 = sp.diff(fd, x, 2)

print("Critical values:", sp.solve(dfd, x))

for i in sp.solve(dfd, x):
    if dfd2.subs(x, i) > 0:
        print("fd has a local mimimum at", i)
    elif dfd2.subs(x, i) < 0:
        print("fd has a local maximum at", i)
    else:
        print("fd is not define")

