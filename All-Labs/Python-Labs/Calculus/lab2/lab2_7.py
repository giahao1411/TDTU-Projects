import numpy as np 

arr1 = np.array([1, 3 , 5, 9, 40, 59])
arr2 = np.array([1, 5, 9, 40, 59, 79])

print(arr1)
print(arr2)
print("Common values of 2 arrays:")
print(np.intersect1d(arr1, arr2))