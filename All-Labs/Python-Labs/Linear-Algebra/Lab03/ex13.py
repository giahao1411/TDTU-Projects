#bai 13

import numpy as np

A = np.random.randint(1, 101, size = (5, 5))
B = np.random.randint(1, 101, size = (5, 5))

print("ma tran A = \n", A)
print("ma tran B = \n", B)

detsumAB = np.linalg.det(np.add(A, B))
detA = np.linalg.det(A)
detB = np.linalg.det(B)

if detsumAB == (detA + detB):
  print("det(A+B) = detA + detB")
else:
  print("det(A+B) != detA + detB")