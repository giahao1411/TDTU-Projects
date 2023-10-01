#bai 9

import numpy as np

T = np.array([
    [0.6, 0.7],
    [0.4, 0.3]
])

p = np.array([
    [0.5],
    [0.5]
])

Tk = np.copy(T)

for k in range(1, 100001):
  pk = np.matmul(Tk, p)
  Tk = np.matmul(Tk, T)
  if k == 1 or k == 2 or k == 10 or k == 100 or k == 100000:
    print("- k = ", k)
    print("pk = ", pk)
  