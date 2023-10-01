#bai 10

import numpy as np

def orthogonal_projection(y, u):
    projection = np.dot(y, u) / np.dot(u, u) * u
    return projection

y = np.array([7, 6])
u = np.array([4, 2])

proj_u_y = orthogonal_projection(y.T, u.T)
print("The orthogonal projection of y on u is:", proj_u_y)