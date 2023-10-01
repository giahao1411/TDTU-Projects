#bai 13 

import numpy as np 

A = np.random.randint(1, 100, size = (10, 10))

B = A[1::2, :]          #('1::2'): chon hang 1 va bo qua 1 hang
                        #(':'): chon tat ca cac cot

print("Matrix A = \n", A)
print("Even rows of the matrix A = \n", B)