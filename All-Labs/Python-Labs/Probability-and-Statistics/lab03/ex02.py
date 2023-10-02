from fractions import Fraction

S = [('Thanh', 'Nữ'), ('Hồng', 'Nữ'), ('Thương', 'Nữ'), ('Đào', 'Nữ'), ('My', 'Nữ'), ('Yến', 'Nữ'), ('Hạnh', 'Nữ'),
     ('My', 'Nữ'), ('Vy', 'Nữ'), ('Tiên', 'Nữ'), ('Thanh', 'Nam'), ('Thanh', 'Nam'), ('Bình', 'Nam'), ('Nhật', 'Nam'), ('Hào', 'Nam'), ('Đạt', 'Nam'), ('Minh', 'Nam')]

# let A is an event that students have their name 'Thanh'
A = []
for i in S:
    if 'Thanh' in i:
        A.append(i)
print(A)

# let B is an event that contain female
B = [s for s in S if 'Nữ' in s]
print(B)

# let A_B is an event that 'Thanh' is female
A_B = [s for s in A if 'Nữ' in s]
print(A_B)

P_A = Fraction(len(A), len(S))
P_B = Fraction(len(B), len(S))
P_A_B = Fraction(len(A_B), len(S))

P_A_with_B = P_A_B / P_B
print("Prob student name 'Thanh' with condition female: ", P_A_with_B)
