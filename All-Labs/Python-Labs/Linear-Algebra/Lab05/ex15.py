#bai 15

import numpy as np

A = np.random.randint(1, 100, size = (10, 10))

B = []

for i in range(A.shape[0]):
  if i % 2 != 0:
    B += [np.flipud(A[i, :])]
  else:
    B += [A[i, :]]

print(A, "\n")
print("\n", np.reshape(B, (10, 10)))