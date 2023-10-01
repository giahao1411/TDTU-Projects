import numpy as np

arr = np.array([1, -8, 9, -56, 5, 45])

print("Origin array:", arr)
print("Replaced array:")
arr[arr < 0] = 0
print(arr)