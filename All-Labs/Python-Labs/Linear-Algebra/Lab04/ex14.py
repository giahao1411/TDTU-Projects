#bai 14

import numpy as np

A = np.random.randint(1, 100, size = (10, 10))

B = []

for i in range(10):
  for j in range(10):
    if A[i][j] % 2 == 0:
      B.append(A[i][j])

print("Matrix A = \n", A)
print("Even integer in the matrix A = \n", B)
