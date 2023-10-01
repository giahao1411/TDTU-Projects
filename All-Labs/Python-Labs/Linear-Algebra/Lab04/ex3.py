#bai 3

import numpy as np
import matplotlib.pyplot as plt 

def plot3DEquation(ax, x_ar, a, b, c, d):
  #ax + by + cz = d
  if c != 0:
    z_func = lambda x, y: (d - a*x - b*y)/c 
    y_ar = x_ar.copy()
    X, Y = np.meshgrid(x_ar, y_ar)
    Z = z_func(X, Y)
    ax.plot_surface(X, Y, Z)
  else:
    #ax + by = d -> y = (d - ax)/b
    if b != 0:        
      y_func = lambda x: (d - a*x)/b
      y_ar = list(map(y_func, x_ar))
      ax.plot_surface(x_ar, y_ar, zdir = 'z', zs = -50)
    else:
      #ax = d -> x = d/a
      if a != 0:
        x_ar_new = np.full(len(x_ar), d/a)
        y_ar = np.linspace(-10, 10, num = len(x_ar))
        ax.plot(x_ar_new, y_ar, zdir = 'z', zs = -50)
      else:
        print("Cannot plot this function!")

x_ar = np.arange(-10, 10.1, 0.1)
fig = plt.figure()
ax = fig.add_subplot(projection = '3d')
plot3DEquation(ax, x_ar, 5, 1, 6, 10)
plot3DEquation(ax, x_ar, 2, 12, 8, 20)
plot3DEquation(ax, x_ar, 3, 9, 3, 1) 

plt.title("System 2")
ax.set_xlim([-10, 10])
ax.set_ylim([-20, 20])
ax.set_zlim([-50, 50])
plt.show()