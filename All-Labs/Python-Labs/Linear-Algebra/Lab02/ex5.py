#bai 5

import numpy as np

#y = np.array([1, 2, 16, 31, 22, 2, 8, 12, 21, 23, 4, 9, 11, 14, 25, 3, 6, 10, 16, 34])
#Y = np.reshape(y, (4, 5))

Y = np.array([
    [1, 2, 16, 31, 22],
    [2, 8, 12, 21, 23],
    [4, 9, 11, 14, 25],
    [3, 6, 10, 16, 34]
])

#cau a - x = (8 12 21) -> x = Y[row, col] 
x = Y[1, 1:4]
print("Cau a:\n", x)

#cau b
y = Y[0:5, 2:3]
print("Cau b:\n", y)

#cau c
A = Y[1:3, 1:4]
print("Cau c:\n", A)

#cau d
B = Y[0:5, 0:5:2]
#B = Y[:, [0,2,4]]
print("Cau d:\n", B)

#cau e
C = Y[1:5, [0,2,3,4]]
print("Cau e:\n", C)

#cau f
D = Y[Y > 12]
print("Cau f:\n", D)