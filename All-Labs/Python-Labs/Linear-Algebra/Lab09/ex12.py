#bai 12
 
import numpy as np 

x = np.array([2015, 2016, 2017, 2018, 2019])  #years
y = np.array([12, 19, 29, 37, 45])            #million dollar

arr_x = np.column_stack((x, np.ones_like(x)))

print("arr_x = \n", arr_x)

res = np.linalg.lstsq(arr_x, y, rcond = None)[0]

print("\n", res)

res1 = round(res[0], 5)
res2 = round(res[1], 5)

print("\nres[1] =", res1)
print("res[2] =", res2)

print("\nThe sale in 2020 =", round((res1 * 2020 + res2), 5))