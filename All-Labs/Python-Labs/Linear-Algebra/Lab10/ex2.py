#bai 2

import numpy as np
from sympy import *
from matplotlib import pyplot as plt

set = np.array([32, 31.9, 31.8, 32.1, 32.2])

for a in set:
   A = np.array([
    [-6, 28, 21],
    [4, -15, -12],
    [8, a, 25]
])
   
   eval, vector = np.linalg.eig(A)
   print("\n- a =", a, "- eigenevalues = ", eval)
   print("eigenvectors = \n", vector)
   print("det = ", round(np.linalg.det(A), 5))

#plot
print("\nPlot\n")
A = np.array([
    [-6, 28, 21],
    [4, -15, -12],
    [8, 0, 15]
])

color = ['b', 'r', 'g', 'k', 'c', 'm']

t = symbols('t')

x = np.arange(0, 3, 0.05)

fig = plt.figure()
i = 0
for i, alp in enumerate(set):
     B = A
     B[2,1] = alp 
     lambd = np.linalg.eigvals(B)
     p = 1
    
     for j in range(len(lambd)):
         p = p*(lambd[j] - t) 
     y = lambdify(t, p, "numpy")(x)
     plt.plot(x, y, color[i])
     i += 1

plt.title("Bai 2")
plt.show()