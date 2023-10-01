import numpy as np 

arr = np.array([1, np.e, 8, np.e**2, np.e**(1/3)])

print("origin arr:", arr)
print("\nnatural log=", np.log(arr))
print("\ncommon log(base 10)=", np.log10(arr))
print("\nbase 2 log=", np.log2(arr))