#bai 4

import numpy as np

#2D in 3D example :Plot function: z = sin(3*x^2 + y^2) with random x, y
import numpy as np
import matplotlib.pyplot as plt

x= np.random.random(100)
y= np.random.random(100)
z= np.sin(3*x**2+y**2)  # z = sin(3*x^2 + y^2)

fig= plt.figure()
ax= fig.add_subplot(111, projection= '3d')
ax.scatter(x,y,z)
ax.plot(x, z, 'r+', zdir='y', zs=1.5)
ax.plot(y, z, 'g+', zdir='x', zs=-0.5)
ax.plot(x, y, 'k+', zdir='z', zs=-1.5)

ax.set_xlim([-0.5, 1.5])
ax.set_ylim([-0.5, 1.5])
ax.set_zlim([-1.5, 1.5])

plt.show()