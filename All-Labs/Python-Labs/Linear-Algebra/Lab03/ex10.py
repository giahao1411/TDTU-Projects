#bai 10 

import numpy as np

A = np.array([
    [-1, 4, 8],
    [-9, 1, 2]
])

B = np.array([
    [5, 8],
    [0, -6],
    [5, 6]
])

C = np.array([
    [-4, 1],
    [6, 5]
])

D = np.array([
    [-6, 3, 1],
    [8, 9, -2],
    [6, -1, 5]
])

#chuyen vi cac ma tran
AT = np.transpose(A)
BT = np.transpose(B)
CT = np.transpose(C)
DT = np.transpose(D)

print("- Cau a: khong lam dc do so cot mtrA != so hang chuyen vi mtrB")
print("- Cau b: ", np.matmul(B, CT))
print("- Cau c: ", C - CT)
print("- Cau d: ", D - DT)
print("- Cau e: ", np.transpose(DT))
print("- Cau f: ", 2*CT)
print("- Cau g: ", AT + B)
print("- Cau h: ", np.transpose(np.add(AT, B)))
print("- Cau i: ", np.transpose(np.subtract(2*AT, 5*B)))
print("- Cau j: ", np.transpose(-1*D))
print("- Cau k: ", np.transpose(-1*D))
print("- Cau l: ", np.transpose(np.matmul(C, C)))
print(" - Cau m: ", np.matmul(CT, CT))