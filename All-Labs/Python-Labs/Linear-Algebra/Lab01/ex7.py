#cau 7

import numpy as np

x = np.array([3, 11, -9, -131, -1, 1, -11, 91, -6, 407, -12, -11, 12, 153, 371])

print("cau a:", np.max(x))                  #tim max
print("cau b:", np.min(x))                  #tim min
print("cau c:", np.where(x > 10))           #tim phan tu > 10
print("cau d:", np.flipud(x))               #dao nguoc vecto
print("cau e", np.sort(x))                  #sap xep tang dan
print("cau f:", np.flipud(np.sort(x)))      #sap xep giam dan

#cau g
count = 0
for i in range(len(x)):
  for j in range(i + 1, len(x)):
    if i != j and x[i] + x[j] == 0:
        count += 1
print("cau g: so lan xi + xj = 0 la:", count)

#cau h 
count1 = 0
for i in range(len(x)):
  for j in range(i + 1, len(x)):
    if x[i] == x[j]:
      count1 += 1
print("cau h: cac phan tu trung nhau la: ", count1)

#cau i
y = []
for i in range(len(x)):
  kq = x[i] + x[len(x) -i - 1]
  y.append(kq)
print("cau i:", np.array(y))

#cau j
w = []

def check_armstrong(n):
  sum = 0
  temp = n
  while temp > 0:
    r = temp % 10
    sum += r**3
    temp //= 10
  if sum == n:
    return True
  else:
    return False

for i in range(len(x)):
  if check_armstrong(x[i]):
    w.append(x[i])

print("cau j", np.array(w))

#cau k
duong = []
for i in range(len(x)):
  if x[i] > 0:
    duong.append(x[i])

print("cau k:", np.array(duong))

#cau l
n = len(x)
median_index = n // 2
if n % 2 == 0:
  median_value = [x[median_index - 1], x[median_index]]
else:
  median_value = [x[median_index]]

print("cau l:", np.array(median_value))

#cau m
sum = 0 
sum1 = 0

for i in range(len(x)):
  sum1 += x[i]
tb = sum1/len(x)

for i in range(len(x)):
  if x[i] < tb:
    sum += x[i]

print("cau m:", sum)

#cau n
rp = x

for i in range(len(x)):
  if x[i] < 0:
    rp[i] = abs(rp[i])

print("cau n:", np.array(rp))