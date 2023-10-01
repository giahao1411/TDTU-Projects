#bai 3

import numpy as np 
import sympy as sp

C = np.array([
    [1, 0, 2, 3],
    [4, -1, 0, 2],
    [0, -1, -8, -10]
])

#cau a
print("----Cau a:----")
res_a = sp.Matrix(C).rref()
print("sp.Matrix(C).rref() = \n", res_a)

basisC = C[:, list(res_a[1])]
print("A basis of column space of C = \n", basisC)

#cau b
print("\n----Cau b:----")
res_b = sp.Matrix(C.T).rref()
print("sp.Matrix(C.T).rref() = \n", res_b)

basisC_T = C.T[:, list(res_b[1])]
print("A basis of row space of C = \n", basisC_T)