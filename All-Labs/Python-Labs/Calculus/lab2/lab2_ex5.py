import numpy as np 

arr1 = [] 
arr2 = []

n = int(input("Enter number of elements:"))

for i in range(0, n):
    ele1 = int(input())
    ele2 = int(input())

    arr1.append(ele1)
    arr2.append(ele2)

print("array 1:", arr1)
print("array 2:", arr2)
print("Unique sorted array of values that are in either of the two input arrays:")
print(np.union1d(arr1, arr2))