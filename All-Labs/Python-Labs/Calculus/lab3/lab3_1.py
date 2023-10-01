import math 

def fa(x):
    return math.sqrt(x)
def fb(x):
    return x**(1/3)
def fc(x):
    return x**(2/3)
def fd(x):
    return x**3/3 - x**2/2 - 2*x + 1/3
def fe(x):
    return (2*x**2 - 3)/(7*x + 4)

ff = lambda x: (5*x**2 + 8*x - 3)/(3*x**2 + 2)
fg = lambda x: math.sin(x)
fh = lambda x: math.cos(x)
fi = lambda x: 3**x
fj = lambda x: 10**(-x)
fk = lambda x: math.e**x
fl = lambda x: math.log2(x)
fm = lambda x: math.log10(x)
fn = lambda x: math.log(x)

print(fa(4))
print(fb(5))
print(fc(6))
print(fd(12))
print(fe(45))
print(ff(44))
print(fg(2))
print(fh(5))
print(fi(12))
print(fj(5))
print(fk(123))
print(fl(12))
print(fm(45))
print(fn(1))