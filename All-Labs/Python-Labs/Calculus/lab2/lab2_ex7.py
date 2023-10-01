import numpy as np 

arr = np.arange(1, 100)

n = arr[(arr % 3 == 0) | (arr % 5 == 0)]
print(n[:1000])
print("Sum of elements multiples for 3 and 5:", n.sum())