import math
import numpy as np 

def fa(x):
    return 2 + (x**2)/(x**2 + 4)
def a():
    for x in np.arange(-2, 2.1, 0.1):
        print(round(fa(x), 7))

def fb(x):
    return (5*x + 10)**(1/2)
def b():
    for x in np.arange(0, 5.1, 0.1):
        print(round(fb(x), 5))

fc = lambda x: 2/(x**2 - 16)
def c():
    for x in np.arange(5, 10.1, 0.1):
        print(round(fc(x), 6))

fd = lambda x: x**4 + 3*x**2 - 1
def d():
    for x in np.arange(-3, 3.1, 0.1):
        print(round(fd(x), 8))

def fe(x):
    if x >= 0:
        return x
    if x < 0:
        return -x
def e():
    for x in np.arange(-3 , 3.1, 0.1):
        print(round(fe(x), 2))

a()
b()
c()
d()
e()
