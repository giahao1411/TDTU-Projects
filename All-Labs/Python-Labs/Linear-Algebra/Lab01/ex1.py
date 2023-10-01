#cau 1:

import numpy as np

x = [1, 3, 5, 2 ,9]
y = [-1, 3, 15, 27, 29]

print(x)
print(y)
print(len(x))
print(len(y))
print("x + y: ", x + y)

vx = np.array(x)    
vy = np.array(y)

print(vx)
print(vy)
print("The number of element in vx:", len(vx))
print("The number of element in vy:", len(vy))
print("vx + vy: ", vx + vy)