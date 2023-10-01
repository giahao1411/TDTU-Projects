#bai 9

import numpy as np 
import matplotlib.pyplot as plt

#house's matrix
pts = np.array([
    [0, 1, 3, 3, 4, 4, 5, 6, 5, 5, 3, 3, 2, 2, 1, 1, 0],
    [2, 3, 3, 4, 4, 3, 3, 2, 2, 0, 0, 1, 1, 0, 0, 2, 2]
])

#----cau a----
#set translation values - dat cac gia tri tinh tien 
dx = 2
dy = 5

#ma tran tinh tien - cong cac gia tri ma tran ban dau vao ma tran tinh tien
transV = [[dx], [dy]]                      
                                          
#ma tran sau khi tinh tien                
trans_pts = np.add(transV, pts)          
print("trans_pts =\n", trans_pts)

#Before translation - truoc tinh tien
plt.plot(pts[0], pts[1],'r-')

#After translation - sau tinh tien
plt.plot(trans_pts[0], trans_pts[1],'go-') 
plt.title("Translation")
plt.show()

#----cau b----
transVb = np.array([
    [np.cos(np.pi/3), -np.sin(np.pi/3)],
    [np.sin(np.pi/3), np.cos(np.pi/3)]
])

trans_ptsb = np.matmul(transVb, pts)
print("trans_ptsb =\n", trans_ptsb)

#Before rotation - truoc khi xoay
plt.plot(pts[0], pts[1], 'r-')

#After rotation - sau khi xoay
plt.plot(trans_ptsb[0], trans_ptsb[1], 'go-')
plt.title("Rotation")
plt.show()

#----cau c----
#set scaling values - dat cac gia tri boi so
Sx = 2
Sy = 3

#ma tran boi so 
transVc = [[Sx], [Sy]]

trans_ptsc = pts * transVc 
print("trans_ptsc =\n", trans_ptsc)

#Before scaling - truoc khi nhan ti le
plt.plot(pts[0], pts[1], 'r-')

#After scaling - sai khi nhan ti le
plt.plot(trans_ptsc[0], trans_ptsc[1], 'go-')
plt.title("Scaling")
plt.show()

#----cau d----
#set shear values - dat cac gia tri ti le 
Sxd = 0.5
Syd = -1.5

#ma tran ti le 
Shearx = np.array([[1, 0],[Sxd, 1]])
Sheary = np.array([[1, Syd],[0, 1]])

#trans_ptsd = np.matmul(Shearx, pts)
trans_ptsd = np.matmul(Sheary, pts)

print("trans_ptsd =\n", trans_ptsd)

#Before shear - truoc khi ti le
plt.plot(pts[0], pts[1], 'r-')

#After shear - sau khi ti le
plt.plot(trans_ptsd[0], trans_ptsd[1], 'go-')
plt.title("Shear")
plt.show()