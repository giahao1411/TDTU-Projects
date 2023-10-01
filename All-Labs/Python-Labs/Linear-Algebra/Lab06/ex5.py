#bai 5

import numpy as np


#cau a
u1 = np.array([2, 3])

unit_u1 = u1/np.linalg.norm(u1)

print("unit vecto of u is", unit_u1, "with 2-norm = ", np.linalg.norm(unit_u1))

#cau b
u2 = np.array([1, 2, 3])

unit_u2 = u2/np.linalg.norm(u2)

print("unit vecto of u is", unit_u2, "with 2-norm = ", np.linalg.norm(unit_u2))

#cau c 
u3 = np.array([1/2, -1/2, 1/4])

unit_u3 = u3/np.linalg.norm(u3)

print("unit vecto of u is", unit_u3, "with 2-norm = ", np.linalg.norm(unit_u3))

#cau d
u4 = np.array([2**(1/2), 2, -2**(1/2), 2**(1/2)])

unit_u4 = u4/np.linalg.norm(u4)

print("unit vecto of u is", unit_u4, "with 2-norm = ", np.linalg.norm(unit_u4))