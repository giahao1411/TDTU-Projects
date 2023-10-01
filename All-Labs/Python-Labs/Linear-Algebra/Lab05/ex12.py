#bai 12

import numpy as np

A = np.random.randint(1, 100, size = (10, 10))

B = A[:, 0::2]

print(A, "\n")
print("\n", B)