#cau 6

import numpy as np

x = np.array([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20])

print("cau a:", x[:6])
print("cau b:", x[6:])
print("cau c:", x[0], x[3], x[-1])          #first-fourth-last
print("cau d:", x[0], x[2], x[4], x[6])     #first-third-fifth-seventh
print("cau e:", x[1::2])                    #phan tu le(vi tri le)
print("cau f:", x[::2])                     #phan tu chan(vi tri chan)