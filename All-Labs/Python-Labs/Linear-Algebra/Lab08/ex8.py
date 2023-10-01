#bai 8 

import numpy as np
import matplotlib.pyplot as plt

#khoi tao vector 
V = np.array([1, 2])

#cau a
pi = np.pi

#Matrix R
R = np.array([
    [np.cos(pi), -np.sin(pi)],
    [np.sin(pi), np.cos(pi)]
])

#ap dung ma tran R vao V -> w
w = R @ V

plt.arrow(0, 0, V[0], V[1], color = "red", width = 0.1, label = "original")
plt.arrow(0, 0, w[0], w[1], color = "blue", width = 0.1, label = "transformed")
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.title("phi = pi")
plt.grid()
plt.legend()
plt.show()

#cau b

R1 = np.array([
    [np.cos(pi/3), -np.sin(pi/3)],
    [np.sin(pi/3), np.cos(pi/3)]
])

w1 = R1 @ V

plt.arrow(0, 0, V[0], V[1], color = "red", width = 0.1, label = "original")
plt.arrow(0, 0, w1[0], w1[1], color = "blue", width = 0.1, label = "transformed")
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.title("phi = pi/3")
plt.grid()
plt.legend()
plt.show()