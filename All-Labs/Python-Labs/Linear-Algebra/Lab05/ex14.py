#bai 14

#A.shape[0]: dong 
#A.shape[1]: cot

import numpy as np 

A = np.random.randint(1, 100, size = (10, 10))
B = []

#for i in range(10):
#   for j in range(10):

for i in range(A.shape[0]):
  for j in range(A.shape[1]):
    if A[i][j] % 2 == 0:
      B.append(A[i, j])

print(A, "\n")
print("\n", B)