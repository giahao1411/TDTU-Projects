#bai 5

import numpy as np 

def checkDiagonalizable(A):
  w, P = np.linalg.eig(A)
  print("w = ", w)
  D = np.diag(w)
  print("D = \n", D)
  print("--------------")
  P_1 = np.linalg.inv(P)

  res = np.matmul(np.matmul(P, D), P_1)
  print("res = \n", res)
  return  np.allclose(A, res)

"""
dieu kien khac de ma tran cheo hoa dc la so tri rieng = so vector rieng
if len(eval_1) == len(vector_1):
  print("ma tran cheo hoa dc")
"""

#cau 1

A1 = np.array([
    [4, -5],
    [2, -3]
])
print("Cau 1:")
if checkDiagonalizable(A1):
  print("--> ma tran cheo hoa duoc")
else:
  print("--> ma tran khong cheo hoa duoc")

#cau 2

A2 = np.array([
    [0, 2],
    [0, 1]
])

print("\nCau 2:")
if checkDiagonalizable(A2):
  print("--> ma tran cheo hoa duoc")
else:
  print("--> ma tran khong cheo hoa duoc")

#cau 3

A3 = np.array([
    [2, 3],
    [1, 4]
])

print("\nCau 3:")
if checkDiagonalizable(A3):
  print("--> ma tran cheo hoa duoc")
else:
  print("--> ma tran khong cheo hoa duoc")

#cau 4

A4 = np.array([
    [1, 2, -2],
    [-2, 5, -2],
    [-6, 6, -3]
])

print("\nCau 4:")
if checkDiagonalizable(A4):
  print("--> ma tran cheo hoa duoc")
else:
  print("--> ma tran khong cheo hoa duoc")

#cau 5

A5 = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

print("\nCau 5:")
if checkDiagonalizable(A5):
  print("--> ma tran cheo hoa duoc")
else:
  print("--> ma tran khong cheo hoa duoc")