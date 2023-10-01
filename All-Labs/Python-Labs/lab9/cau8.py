import sympy as sp 

x = sp.symbols("x")

def golden_search(fx, a, b, z): 
    d = b - a 
    while b - a >= z:
        d = 0.618 * d 
        x1 = b - d 
        x2 = a + d
        if(fx.subs(x, x1) <= fx.subs(x, x2)):
            b = x2
        else: 
            a = x1
    return (a + b)/2 

# a: 
a = -5
b = 5 
fx = -2*(x**2) + x + 4
z = 1/9

print(golden_search(fx, a, b, z))
sp.plot(fx, (x, a, b))

# b: 
a = -6
b = 6
fx = -4*(x**2) + 2*x + 2
z = 1/10

print(golden_search(fx, a, b, z))
sp.plot(fx, (x, a, b))

# c: 
a = -5
b = -2
fx = x**3 + 6*(x**2) + 5*x - 12
z = 1/10

print(golden_search(fx, a, b, z))
sp.plot(fx, (x, a, b))

# d: 
a = 0
b = 3
fx = 2*x - x**2
z = 1/100

print(golden_search(fx, a, b, z))
sp.plot(fx, (x, a, b))

# e: 
a = -10
b = 10
fx = x**2 - x
z = 1/5

print(golden_search(fx, a, b, z))
sp.plot(fx, (x, a, b))
  
# f: 
a = -10
b = 10
fx =-(x+6)**2 + 4
z = 1/8

print(golden_search(fx, a, b, z))
sp.plot(fx, (x, a, b))

# g: 
a = -3
b = 5
fx = -2*(x**2) + 3*x + 6 
z = 1/8

print(golden_search(fx, a, b, z))
sp.plot(fx, (x, a, b))