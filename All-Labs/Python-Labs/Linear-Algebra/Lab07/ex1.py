#bai 1

import numpy as np

#ham kiem tra co la to hop tuyen tinh hay khong
def isCombination(vector, w):
  rank = np.linalg.matrix_rank(vector)
  rankw = np.linalg.matrix_rank(np.column_stack((vector, w)))
  if rank == rankw:
    return True
  else:
    return False

#cau a
v1a = np.array([1, 2, 3, 4])
v2a = np.array([-1, 0, 1, 3])
v3a = np.array([0, 5, -6, 8])

Aa = np.array([v1a, v2a, v3a]).T

wa = np.array([3, -6, 17, 11]).T

if isCombination(Aa, wa):
  print("a. is combination")
else:
  print("a. is not combination")

#cau b
v1b = np.array([1, 1, 2, 2])
v2b = np.array([2, 3, 5, 6])
v3b = np.array([2, -1, 3, 6])

Ab = np.array([v1b, v2b, v3b]).T

wb = np.array([0, 5, 3, 0])

if isCombination(Ab, wb):
  print("b. is combination")
else:
  print("b. is not combination")

#cau c
v1c = np.array([1, 1, 2, 2])
v2c = np.array([2, 3, 5, 6])
v3c = np.array([2, -1, 3, 6])

Ac = np.array([v1c, v2c, v3c]).T

wc = np.array([-1, 6, 1, -4])

if isCombination(Ac, wc):
  print("c. is combination")
else:
  print("c. is not combination")

#cau d
v1d = np.array([1, 2, 3, 4])
v2d = np.array([-1, 0, 1, 3])
v3d = np.array([0, 5, -6, 8])
v4d = np.array([1, 15, -12, 8])

Ad = np.array([v1d, v2d, v3d, v4d]).T

wd = np.array([0, -6, 17, 11])

if isCombination(Ad, wd):
  print("d. is combination")
else:
  print("d. is not combination")