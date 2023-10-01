import numpy as np 

arr = []

n = int(input("enter number of elements:"))

for i in range(0, n):
    ele = int(input())

    arr.append(ele)

print(arr)
print("Number of non zero element in an array:")
print(np.count_nonzero(arr))
