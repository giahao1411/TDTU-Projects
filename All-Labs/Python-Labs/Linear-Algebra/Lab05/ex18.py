#bai 18

import numpy as np

A = np.random.randint(1, 100, size = (10, 10))

sum = 0

#sum dong dau
for i in range(A.shape[1]):
  sum += A[0, i]

#sum cot dau
for i in range(1, A.shape[0]):
  sum += A[i, 0]

#sum dong cuoi
for i in range(1, A.shape[1] - 1):
  sum += A[A.shape[0] - 1, i]

#sum cot cuoi
for i in range(1, A.shape[0]):
  sum += A[i, A.shape[0] - 1]

print(A, "\n")
print("sum = ", sum)