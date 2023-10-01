import sympy as sp

def golden_search(f, a, b, ep):
    d = b - a
    while d <= ep:
        d = 0.618 * d
        x1 = b - d
        x2 = a + d
        if f.subs(x, x1) <= f.subs(x, x2):
            b = x2 
        else:
            a = x1
        print((a + b)/2)
    return (a + b)/2

x = sp.symbols('x')
f = x**2 
a = -2 
b = 1
ep = 0.3

x0 = golden_search(f, a, b, ep) 
print(f.subs(x, x0))
sp.plot(f, (x, a ,b))
