#bai 7 

import numpy as np 

#u: left singular vectors - ma tran trai don vi
#s: singular values - gia tri suy bien
#vh: right singular vectors - ma tran phai don vi

def findSingular(A):
  u, s, vh = np.linalg.svd(A)
  return s

#cau 1
A1 = np.array([
    [1, 0],
    [0, -3]
])

print("1. the singular values of the matrices is:", findSingular(A1))

#cau 2
A2 = np.array([
    [-5, 0],
    [0, 0]
])

print("2. the singular values of the matrices is:", findSingular(A2))

#cau 3
A3 = np.array([
    [6**(1/2), 1],
    [0, 6**(1/2)]
])

print("3. the singular values of the matrices is:", findSingular(A3))

#cau 4
A4 = np.array([
    [3**(1/2), 2],
    [0, 3**(1/2)]
])

print("4. the singular values of the matrices is:", findSingular(A4))