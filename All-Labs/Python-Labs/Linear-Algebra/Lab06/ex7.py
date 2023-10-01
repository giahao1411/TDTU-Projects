#bai 7

#np.linalg.inv(): tim ma tran nghich dao 

import numpy as np

E = np.array([
    [80, 98, 99, 85, 106, 94],
    [71, 92, 76, 95, 100, 92],
    [124, 163, 140, 160, 176, 161]
])

A = np.array([
    [1, 2, 3],
    [2, 1, 2],
    [3, 2, 4]
])

D = np.matmul(np.linalg.inv(A), E)
print(D, "\n")

msg = ""

for col in range(D.shape[1]):
  for row in range(D.shape[0]):
    if int(round(D[row, col], 0)) == 30:
      msg += " "
    else:
      msg += chr(65 + int(round(D[row, col], 0)) - 4)

print(msg)