#bai 8

import numpy as np

# Create the Hilbert matrix A with size 5
A = np.array([[1/(i+j-1) for j in range(1,6)] for i in range(1,6)])
print("Hilbert Matrix = \n", A)

# Create matrix B
B = np.zeros((5,5))
for i in range(5):
    for j in range(i+1):
        if j == 0 or j == i:
            B[i][j] = 1
        else:
            B[i][j] = B[i-1][j-1] + B[i-1][j]

print("\nPascal Matrix = \n", B)

# Create magic matrix C
n = 5
C = [[0 for x in range(n)] for y in range(n)]

i = n // 2
j = n - 1

num = 1
while num <= (n * n):
    if i == -1 and j == n:  
        j = n - 2
        i = 0
    else:
        if j == n:
            j = 0
        if i < 0:
            i = n - 1
    if C[i][j]:
        j -= 2
        i += 1
        continue
    else:
        C[i][j] = num
        num += 1
    j += 1
    i -= 1

arr = np.array(C).flatten()
# Reshape to square matrix
n = int(np.sqrt(len(arr)))
C_square = arr.reshape(n, n)
print("\nMagic matrix = \n", C_square)

# Find a basis for the null space of Hilbert Matrix
u, s, vh = np.linalg.svd(A)
null_space_basis_A = vh[np.sum(s > 1e-10):,:].T

# Find a basis for the null space of Pascal Matrix
u, s, vh = np.linalg.svd(B)
null_space_basis_B = vh[np.sum(s > 1e-10):,:].T

# Find a basis for the null space of Magic Matrix
u, s, vh = np.linalg.svd(C_square)
null_space_basis_C = vh[np.sum(s > 1e-10):,:].T

print("\nBasis for the null space of Hilbert Matrix:", null_space_basis_A)

print("Basis for the null space of Pascal Matrix:", null_space_basis_B)

print("Basis for the null space of Magic Matrix:", null_space_basis_C)