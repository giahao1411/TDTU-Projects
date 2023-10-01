#bai 11

import numpy as np

A = np.array([
    [2, 4, 1],
    [6, 7, 2],
    [3, 5, 9]
])

#cau a - check co phai ma tran vuong
print("Cau a: ", A.shape)        #(var).shape tra ve (row, column) cua ma tran
if A.shape[0] == A.shape[1]:
  print("A la ma tran vuong")
else:
  print("A khong la ma tran vuong")

#cau b - check co phai ma tran doi xung
print("Cau b: ")
if np.allclose(A.T, A):         #np.allclose(var, var): so sanh 2 ma tran co = k -> tra ve boolean
  print("A la ma tran doi xung")
else:
  print("A khong la ma tran doi xung")

#cau c - check co phai ma tran doi xung lech
print("Cau c: ")
if np.allclose(A.T, -1*A):
  print("A la ma tran doi xung lech")
else:
  print("A khong la ma tran doi xung lech")

#cau d - tim ma tran tam giac tren
print("Cau d:")
print(np.triu(A))             #np.triu(var) tra ve ma tran tam giac tren

#cau e - tim ma tran tam giac duoi
print("Cau e:")
print(np.tril(A))             #np.tril(var) tra ve ma tran tam giac duoi