#bai 12

import numpy as np

A = np.random.randint(1, 100, size = (10, 10))

B = A[:, 0::2]        #(':'): chon tat ca cac hang
                      #('0::2'): chon cot 0 va bo qua 1 cot
                      
print("Matrix A = \n", A)
print("Odd columns of the matrix A = \n", B)