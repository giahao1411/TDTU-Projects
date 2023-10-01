#bai 8:

import numpy as np

P = np.array([2, 1, 3])   #S - V - C
S = np.array([
    [12, 15, 10, 16, 12],
    [5, 9, 14, 7, 10],
    [8, 12, 10, 9, 15]
])

# DT = P.dot(S)
DT = np.matmul(P, S)
print("Monday to Friday total sale for each day:\n", DT)