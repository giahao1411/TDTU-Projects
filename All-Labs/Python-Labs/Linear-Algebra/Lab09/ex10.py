#bai 10

import numpy as np 
import matplotlib.pyplot as plt 

pts = np.array([
    [1, 3, 1, 1],
    [1, 1, 3, 1]
])

#np.eye: tao ma tran don vi cap n
I = np.eye(2)

I_pts = np.matmul(-I, pts)

#before
plt.plot(pts[0], pts[1], 'r-')

#after 
plt.plot(I_pts[0], I_pts[1], 'go-')
plt.title("Translation")
plt.show()