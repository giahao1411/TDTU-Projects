import numpy as np 
import matplotlib.pyplot as plt 
import math

x = np.arange(-6, 6.1, 0.1)
y = x.copy()

#2a
print("Cau 2a:\n")
fa = lambda x, y: np.cos(x)*np.cos(y)*math.e**(-((x**2 + y**2)**1/2)/4)

X_a, Y_a = np.meshgrid(x, y)

print(X_a)
print(Y_a)

Z_a = fa(X_a, Y_a)

ax = plt.axes(projection = '3d')
ax.plot_surface(X_a, Y_a, Z_a, cmap = 'spring', linewidth = 0)
ax.set_title('Surface plot')
plt.show() 

#2b 
print("Cau 2b:\n")
fb = lambda x, y: -(x*y**2)/(x**2 + y**2)

X_b, Y_b = np.meshgrid(x, y)

print(X_b)
print(Y_b)

Z_b = fb(X_b, Y_b)

bx = plt.axes(projection = '3d')
bx.plot_surface(X_b, Y_b, Z_b, cmap = 'hot', linewidth = 0)
bx.set_title('Surface plot')
plt.show()

#2c
print("Cau 2c:\n")
fc = lambda x, y: (x*y*(x**2 - y**2))/(x**2 + y**2)

X_c, Y_c = np.meshgrid(x, y)

print(X_c)
print(Y_c)

Z_c = fc(X_c, Y_c)

cx = plt.axes(projection = '3d')
cx.plot_surface(X_c, Y_c, Z_c, cmap = 'winter', linewidth = 0)
cx.set_title('Surface plot')
plt.show()

#2d
print("Cau 2d:\n")
fd = lambda x, y: y**2 - y**4 - x**2 

X_d, Y_d = np.meshgrid(x, y)

print(X_d)
print(Y_d)

Z_d = fd(X_d, Y_d)

dx = plt.axes(projection = '3d')
dx.plot_surface(X_d, Y_d, Z_d, cmap = 'cool', linewidth = 0)
dx.set_title('Surface plot')
plt.show()