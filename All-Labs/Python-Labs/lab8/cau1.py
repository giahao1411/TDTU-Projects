f_a_xy = lambda x, y: x**2 + x*y**3 

print(f_a_xy(0, 0))
print(f_a_xy(-1, 1))
print(f_a_xy(2, 3))
print(f_a_xy(-3, -2))

print("-------")

f_b_xy = lambda x, y, z: (x - y)/(y**2 + z**2)
print(f_b_xy(3, -1, 2))
print(f_b_xy(1, 1/2, 1/4))
print(f_b_xy(0, -1/3, 0))
print(f_b_xy(2, 2, 100))

