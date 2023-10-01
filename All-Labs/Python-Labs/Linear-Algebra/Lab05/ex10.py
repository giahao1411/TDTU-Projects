#bai 10 

#np.eye(...): khai bao ma tran don vi cap (...)

import numpy as np  

A = np.array([
    [0.25, 0.15, 0.1],
    [0.4, 0.15, 0.2],
    [0.15, 0.2, 0.2]
])

d = np.array([[100], [100], [100]])     #matrix
#d = np.array([100, 100, 100]): vecto  

print("p = \n", np.matmul(np.linalg.inv(np.eye(3) - A), d))