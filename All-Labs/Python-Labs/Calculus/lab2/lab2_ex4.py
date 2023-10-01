import numpy as np 

arr1 = []
arr2 = []

n = int(input("Enter number of elements:"))
print("Enter arr1 and arr2:")

for i in range(0, n):
    ele1 = int(input())
    ele2 = int(input())

    arr1.append(ele1)
    arr2.append(ele2)

print("array 1:", arr1)
print("array 2:", arr2)
print("Unique values in arr1 that not in arr2:")
print(np.setdiff1d(arr1, arr2))