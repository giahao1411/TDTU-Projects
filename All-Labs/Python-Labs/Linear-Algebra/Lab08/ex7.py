#bai 7

import numpy as np
import matplotlib.pyplot as plt

#khai bao vector x thuoc R2
x = np.array([2, 3])

#cau a
print("Cau a:")

#sau khi nhan S
S1 = np.array([
    [2, 0],
    [0, 2]
])

x1 = np.matmul(x, S1)

plt.arrow(0, 0, x1[0], x1[1], color = "blue", width = 0.1, label = "transformed")
plt.arrow(0, 0, x[0], x[1], color = "red", width = 0.1, label = "original")
plt.xlim(-1, 10)
plt.ylim(-1, 10)
plt.title("Cau a")
plt.grid()
plt.legend()
plt.show()

#cau b
print("Cau b:")

#Sau khi nhan S
S2 = np.array([
    [0.5, 0],
    [0, 0.5]
])

x2 = np.matmul(x, S2)

plt.arrow(0, 0, x[0], x[1], color = "red", width = 0.1, label = "original")
plt.arrow(0, 0, x2[0], x2[1], color = "blue", width = 0.1, label = "transformed")
plt.xlim(-1, 10)
plt.ylim(-1, 10)
plt.title("Cau b")
plt.grid()
plt.legend()
plt.show()

#cau c
print("Cau c:")

#Sau khi nhan S
S3 = np.array([
    [1, 0],
    [0, -1]
])

x3 = np.matmul(x, S3)

plt.arrow(0, 0, x[0], x[1], color = "red", width = 0.1, label = "original")
plt.arrow(0, 0, x3[0], x3[1], color = "blue", width = 0.1, label = "transformed")
plt.xlim(-1, 10)
plt.ylim(-10, 10)
plt.title("Cau c")
plt.grid()
plt.legend()
plt.show()

#cau d
print("Cau d:")

#Sau khi nhan S
S4 = np.array([
    [-1, 0],
    [0, 1]
])

x4 = np.matmul(x, S4)

plt.arrow(0, 0, x[0], x[1], color = "red", width = 0.1, label = "original")
plt.arrow(0, 0, x4[0], x4[1], color = "blue", width = 0.1, label = "transformed")
plt.xlim(-10, 10)
plt.ylim(-1, 10)
plt.title("Cau d")
plt.grid()
plt.legend()
plt.show()