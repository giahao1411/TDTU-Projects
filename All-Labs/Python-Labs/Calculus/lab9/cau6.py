import sympy as sp 

x = sp.symbols('x')

def Fibonacci_Search(f, a, b, z):
    f1 = 2
    f2 = 3 
    while (b - a) >= z: 
        d = b - a 
        x1  = b - d *(f1/f2)
        x2  = a + d *(f1/f2)
        if f.subs(x, x1) <= f.subs(x, x2):
            b = x2 
        else:
            a = x1 

        temp = f1 
        f1 = f2 
        f2 = f1 + temp
    return (a + b)/2

f = x**2
a = -2 
b = 1
z = 0.3   

x0 = Fibonacci_Search(f, a,b,z)
sp.plot(f,(x,a,b))