#bai 19

import numpy as np

A = np.random.randint(1, 100, size = (10, 10))
B = np.flipud(A)

print(A, "\n")

dc1 = np.diag(A)
dc2 = np.diag(B)

sum = 0
for i in range(len(dc1)):
  sum += dc1[i]
for i in range(len(dc2)):
  sum += dc2[i]

print("Sum = ", sum - A[A.shape[0]//2, A.shape[1]//2])