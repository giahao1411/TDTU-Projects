#bai 11

import numpy as np
import matplotlib.pyplot as plt

# 1st row is x-values, and 2nd row is y-values
pts = np.array([
    [2, 2, -3, -3, -2,   -2,    0, 0.0, -2.0, -2, 2],
    [4, 5,  5, -5, -5, -0.5, -0.5, 0.5,  0.5,  4, 4]
])

pts = np.vstack((pts, np.ones(pts.shape[1])))

print(pts)

T2 = [[-1,  0, 0],
      [ 0, -1, 0],
      [ 0,  0, 1]]
transform_pts = np.matmul(T2, pts)

f = plt.figure()
f.set_figwidth(5)
f.set_figheight(5)

plt.fill(pts[0], pts[1],'b')
plt.fill(transform_pts[0], transform_pts[1],'r')
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.grid(linestyle = '--')

plt.show()