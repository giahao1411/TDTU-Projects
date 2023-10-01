import sympy as sp

x = sp.symbols('x')

#cau a -----------------------------------------
fa = x**3 - 27*x

dfa = sp.diff(fa, x)

cvals_a = sp.solve(dfa, x)
print("Critical values:", cvals_a)

for x_a in cvals_a:
    if x_a < 0 or x_a > 5:
        cvals_a.remove(x_a)
cvals_a.extend([0, 5])

yvals_a = [fa.subs(x, a) for a in cvals_a]
print("The absolute maximum is:", max(yvals_a))
print("The absolute mimimum is:", min(yvals_a))

#cau b -----------------------------------------
fb = 3/2*x**4 - 4*x**3 + 4

dfb = sp.diff(fb, x)

cvals_b = sp.solve(dfb, x)
print("Critical values:", cvals_b)

for x_b in cvals_b:
    if x_b < 0 or x_b > 3:
        cvals_b.remove(x_b)
cvals_b.extend([0, 3])

yvals_b = [fb.subs(x, b) for b in cvals_b]
print("The absolute maximum is:", max(yvals_b))
print("The absolute mimimum is:", min(yvals_b))

#cau c -----------------------------------------
fc = 1/2*x**4 - 4*x**2 + 5

dfc = sp.diff(fc, x)

cvals_c = sp.solve(dfc, x)
print("Critical values:", cvals_c)

for x_c in cvals_c:
    if x_c < 1 or x_c > 3:
        cvals_c.remove(x_c)
cvals_c.extend([1, 3])

yvals_c = [fc.subs(x, c) for c in cvals_c]
print("The absolute maximum is:", max(yvals_c))
print("The absolute mimimum is:", min(yvals_c))

#cau d -----------------------------------------
fd = 5/2*x**4 - 20/3*x**3 + 6

dfd = sp.diff(fd, x)

cvals_d = sp.solve(dfd, x)
print("Critical values:", cvals_d)

for x_d in cvals_d:
    if x_d < -1 or x_d > 3:
        cvals_d.remove(x_d)
cvals_d.extend([-1, 3])

yvals_d = [fd.subs(x, d) for d in cvals_d]
print("The absolute maximum is:", max(yvals_d))
print("The absolute mimimum is:", min(yvals_d))
