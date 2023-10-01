#bai 1

import numpy as np

x = np.array([1, 2, 3, 4, 5])
b = np.array([1, 2, 3, 4, 5, 6])
c = np.array([i for i in range(1, 31)])
d = np.array([i for i in range(1, 26)])

#cau a
A = np.tile(x, (4, 1))
A1 = np.transpose(A)

#cau b
B = np.tile(b, (6, 1))

#cau c
C = np.reshape(c, (6, 5))
C1 = np.transpose(C)

#cau d
D = np.reshape(d, (5, 5))

print("Cau a:\n", A1)
print("Cau b:\n", B)
print("Cau c:\n", C1)
print("Cau d:\n", D)