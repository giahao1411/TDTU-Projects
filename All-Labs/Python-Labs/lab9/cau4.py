import sympy as sp 
import numpy as np 
import matplotlib.pyplot as plt

x = sp.symbols('x')

#a
def plot_graph(fa, a, b, xs, ys):
    lx = np.linspace(a,b,1000)
    ly = [fa.subs(x, it).evalf() for it in lx]
    plt.plot(lx, ly)
    plt.scatter(xs, ys)
    plt.show()

fa = x*x - 2*x - 5
a,b = 0, 2

print('f =', fa)
print('a, b = ', a,b)

dfa = fa.diff()
print("f'= ", dfa)

lx = sp.solve(dfa)
print(lx)

lx = np.array([x0 for x0 in lx if a <= x0 and x0 <= b] + [a, b])
print(lx)

ly = np.array([fa.subs(x, x0).evalf() for x0 in lx])
print(ly)

indices = np.array([np.argmin(ly), np.argmax(ly)])
print(indices)

xs = lx[indices]
ys = ly[indices]

plot_graph(fa, a, b, xs, ys)

#b
def plot_graph(fb, a, b, xs, ys):
    lx = np.linspace(a,b,1000)
    ly = [fb.subs(x, it).evalf() for it in lx]
    plt.plot(lx, ly)
    plt.scatter(xs, ys)
    plt.show()

fb = 3*x + x**3 +5
a,b = -4, 4

print('f =', fb)
print('a, b = ', a,b)

dfb = fb.diff()
print("f'= ", dfb)


lx = sp.solve(dfb)
print(lx)

lx = np.array([x0 for x0 in lx if a <= x0 and x0 <= b] + [a, b])
print(lx)

ly = np.array([fa.subs(x, x0).evalf() for x0 in lx])
print(ly)

indices = np.array([np.argmin(ly), np.argmax(ly)])
print(indices)

xs = lx[indices]
ys = ly[indices]

plot_graph(fb, a, b, xs, ys)

#c
def plot_graph(fc, a, b, xs, ys):
    lx = np.linspace(a,b,1000)
    ly = [fc.subs(x, it).evalf() for it in lx]
    plt.plot(lx, ly)
    plt.scatter(xs, ys)
    plt.show()

fc = sp.sin(x) + 3*x**2
a,b = -2, 2

print('f =', fc)
print('a, b = ', a,b)

dfc = fc.diff()
print("f'= ", dfc)

lx = sp.solve(dfc)
print(lx)

lx = np.array([x0 for x0 in lx if a <= x0 and x0 <= b] + [a, b])
print(lx)

ly = np.array([fc.subs(x, x0).evalf() for x0 in lx])
print(ly)

indices = np.array([np.argmin(ly), np.argmax(ly)])
print(indices)

xs = lx[indices]
ys = ly[indices]

plot_graph(fc, a, b, xs, ys)

#d
def plot_graph(fd, a, b, xs, ys):
    lx = np.linspace(a,b,1000)
    ly = [fd.subs(x, it).evalf() for it in lx]
    plt.plot(lx, ly)
    plt.scatter(xs, ys)
    plt.show()

fd = sp.exp(x**2) + 3*x
a,b = -1, 1

print('f =', fd)
print('a, b = ', a,b)

dfd = fd.diff()
print("f'= ", dfd)

lx = sp.solve(dfd)
print(lx)

lx = np.array([x0 for x0 in lx if a <= x0 and x0 <= b] + [a, b])
print(lx)

ly = np.array([fa.subs(x, x0).evalf() for x0 in lx])
print(ly)

indices = np.array([np.argmin(ly), np.argmax(ly)])
print(indices)

xs = lx[indices]
ys = ly[indices]

plot_graph(fd, a, b, xs, ys)