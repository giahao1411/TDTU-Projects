#bai 4

import numpy as np 

#cau a
u_a = np.array([1, 1])
v_a = np.array([0, 1])

a_angle = u_a.dot(v_a)/(np.linalg.norm(u_a) * np.linalg.norm(v_a))

print("a. angle between u and v is", round(np.degrees(np.arccos(a_angle)), 5), "degree")

#cau b
u_b = np.array([1, 0])
v_b = np.array([0, 1])

b_angle = u_b.dot(v_b)/(np.linalg.norm(u_b) * np.linalg.norm(v_b))

print("b. angle between u and v is", round(np.degrees(np.arccos(b_angle)), 5), "degree")

#cau c
u_c = np.array([-2, 3])
v_c = np.array([1/2, -1/2])

c_angle = u_c.dot(v_c)/(np.linalg.norm(u_c) * np.linalg.norm(v_c))

print("c. angle between u and v is", round(np.degrees(np.arccos(c_angle)), 5), "degree")