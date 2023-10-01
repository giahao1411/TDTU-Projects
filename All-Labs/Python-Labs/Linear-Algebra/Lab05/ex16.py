#bai 16

import numpy as np

A = np.random.randint(1, 100, size = (10, 10))
B = A.copy()

max = -1

for i in range(A.shape[0]):
  for j in range(A.shape[1]):
    if A[i, j] % 2 != 0:
      if A[i, j] > max:
        max = A[i, j]

for i in range(B.shape[0]):
  for j in range(B.shape[1]):
    if B[i, j] % 2 != 0:
      B[i, j] = max

print(A, "\n")
print("\n", B)