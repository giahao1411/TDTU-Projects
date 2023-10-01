import numpy as np
import matplotlib.pyplot as plt 

def fa(x, k):
    return x**2 + k
def a():
    k = np.array([2, 4, 6, 8, 10, 12])
    x = np.arange(-10, 10.1, 0.1)

    for ki in k:
        y = [] 
        for xi in x:
            y.append(fa(xi, ki))
        plt.plot(x, y, label = "k=" + str(ki))

    plt.title('Cau a')
    plt.legend()
    plt.show()

def fb(x, k):
    return (x + k)**2 
def b():
    k = np.array([2, 4, 6, 8, 10, 12])
    x = np.arange(-10, 10.1, 0.1)

    for ki in k:
        y = []
        for xi in x:
            y.append(fb(xi ,ki))
        plt.plot(x, y, label = "k=" + str(ki))
    
    plt.title('Cau b')
    plt.legend()
    plt.show()

def fc(x, k):
    return k*x**(1/2)
def c():
    k = np.array([1/3, 1, 3, 6])
    x = np.arange(1, 50.1, 0.1)

    for ki in k:
        y = []
        for xi in x:
            y.append(fc(xi, ki))
        plt.plot(x, y, label = "k=" + str(ki))

    plt.title('Cau c')
    plt.legend()
    plt.show()

def d():
    fd = lambda x: x**3 

    x = np.arange(-100, 100.1, 0.1)
    y = np.array(list(map(fd, x)))

    plt.plot(x, y, label = "orgininal graph")
    plt.plot(x - 1, y - 1, label = "shifted graph")

    plt.title('Cau d')
    plt.legend()
    plt.show()

def e():
    fe = lambda x: x**(2/3)

    x = np.arange(-100, 100.1, 0.1)
    y = np.array(list(map(fe, x)))

    plt.plot(x, y, label ="original graph")
    plt.plot(x + 1, y - 1, label = "shifted graph")

    plt.title('Cau e')
    plt.legend()
    plt.show()

def f():
    ff = lambda x: 1/2*(x + 1) + 5

    x = np.arange(-100, 100.1, 0.1)
    y = np.array(list(map(ff, x)))

    plt.plot(x, y, label = "original graph")
    plt.plot(x + 1, y - 5, label = "shifted graph")

    plt.title('Cau f')
    plt.legend()
    plt.show()

def g():
    fg = lambda x: 1/(x**2)

    x = np.arange(-100, 100.1, 0.1)
    y = np.array(list(map(fg, x)))

    plt.plot(x, y, label = "original graph")
    plt.plot(x - 2, y - 1, label = "shifted graph")

    plt.title('Cau g')
    plt.legend()
    plt.show()

def h():
    fh = lambda x: 1 - x**3

    x = np.arange(-100, 100.1, 0.1)
    y = np.array(list(map(fh, x)))

    plt.plot(x, y, label = "original graph")
    plt.plot(2*x, y, label = "stretched horizontally graph")

    plt.title('Cau h')
    plt.legend()
    plt.show()

def i():
    fi = lambda x: (x + 1)**(1/2)

    x = np.arange(-100, 100.1, 0.1)
    y = np.array(list(map(fi, x)))

    plt.plot(x, y, label = "original graph")
    plt.plot(x/4, y, label = "compressed horizontally graph")

    plt.title('Cau i')
    plt.legend()
    plt.show()

def j():
    fj = lambda x: (x + 1)**(1/2)

    x = np.arange(-100, 100.1, 0.1)
    y = np.array(list(map(fj, x)))

    plt.plot(x, y , label = "original graph")
    plt.plot(x, 3*y, label = "stretched vertically graph")

    plt.title('Cau j')
    plt.legend()
    plt.show()

a()
b()
c()
d()
e()
f()
g()
h()
i()
j()
