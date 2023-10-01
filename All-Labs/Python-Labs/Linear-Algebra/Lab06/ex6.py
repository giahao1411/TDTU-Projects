#bai 6

import numpy as np

v1 = np.array([1, 2, 3])
s2 = np.array([7, 4, 3])
s3 = np.array([2, 1, 9])

# tich do dai 2 diem tru nhau = khoang cach giua 2 diem
distant_v1_s2 = np.linalg.norm(v1 - s2)
distant_v1_s3 = np.linalg.norm(v1 - s3)
distant_s2_s3 = np.linalg.norm(s2 - s3)

print("Distant between v1 and s2 =", distant_v1_s2)
print("Distant between v1 and s3 =", distant_v1_s3)
print("Distant between s2 and s3 =", distant_s2_s3)