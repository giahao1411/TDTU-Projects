#bai 2

import matplotlib.pyplot as plt 
import numpy as np

def plot2DEquation(x_arr, a, b, c):
  # ax + by = c - trong do x thuoc x_ar -> y = (c - ax)/b
  if b != 0:          #ax + by = c
    fx = lambda x: (c - a*x)/b                     #y = fx
    y_ar = list(map(fx, x_arr))
    plt.plot(x_ar, y_ar, label = str(a)  + "x + " + str(b) + "y = " + str(c))
    plt.legend()
  else:               #ax = c
    if a != 0:
      x_ar_new = np.full(len(x_ar), c/a)            #x = c/a
      print("x_ar_new = ", x_ar_new)
      y_ar = np.linspace(-10, 10, num = len(x_ar))
      plt.plot(x_ar_new, y_ar)
    else:
      print("Cannot plot this function!")

x_ar = np.arange(-10, 10.1, 0.1)

#2 duong thang song song - he so goc bang nhau -> y = -(a/b)*x + c/b
plt.title("No solution")
plot2DEquation(x_ar, -1, 1, 3)
plot2DEquation(x_ar, 3, -3, 6)

#2 duong thang trung nhau: a1, b1, c1 trung (a1, b1, c1)*k
plt.show()
plt.title("infinitely solution")
plot2DEquation(x_ar, 2, 3, 4)
plot2DEquation(x_ar, 4, 6, 8)

#2 duong thang giao nhau:
plt.show()
plt.title("Unique solution")
plot2DEquation(x_ar, 3, 4, 6)
plot2DEquation(x_ar, 3, -8, 4)