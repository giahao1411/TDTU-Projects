#bai 14

import numpy as np

A = np.random.randint(1, 101, size = (5, 5))
B = np.random.randint(1, 101, size = (5, 5))

print("ma tran A = \n", A)
print("ma tran B = \n", B)

detmulAB = np.linalg.det(np.matmul(A, B))
detA = np.linalg.det(A)
detB = np.linalg.det(B)

if detmulAB == (detA * detB):
  print("det(AB) = detA*detB")
else:
  print("det(AB) != detA*detB")