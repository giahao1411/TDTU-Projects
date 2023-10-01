#bai 17

import numpy as np

A = np.random.randint(1, 100, size = (10, 10))
B = A.copy()

B[:, 0] = A[:, 9]       #doi cot dau thanh cot cuoi
B[:, 9] = A[:, 0]       #doi cot cuoi thanh cot dau

print(A, "\n")
print("\n", B)