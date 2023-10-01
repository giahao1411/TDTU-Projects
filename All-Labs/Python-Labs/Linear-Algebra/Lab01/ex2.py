#cau 2:

import numpy as np 

n = int(input("Nhap vao n: "))

b = [12 + i*2 for i in np.arange(0, n)]
c = [31 + i*2 for i in np.arange(0, n)]
x = [int(-n/2) + i for i in np.arange(0, n)]
y = [int(n/2) - i for i in np.arange(0, n)]
z = [10 - 2*i for i in np.arange(0, 8)]
w = [1/2**i for i in np.arange(0, n)]

#cau g
list_fibo = [1, 1]
for i in range(2, n):
  list_fibo.append(list_fibo[i - 2] + list_fibo[i - 1])

d = [1/list_fibo[i] for i in np.arange(0, n)]

#cau h
list_prime = []

#tim so nguyen to nho hon n
for num in range(2, n):
  is_prime = True
  for i in range(2, int(num**(1/2) + 1)):
    if num % i == 0:
      is_prime = False
      break
  if is_prime:
    list_prime.append(num)

e = []
for i in list_prime:
  kq = 1/i
  e.append(kq)

#cau i
a = [int(i*(i+1)/2) for i in range(1, n)]

#cau j
list = [2, 5, 10]
step = 7
for i in range(2, n):
  kq = list[i] + step
  step = step + 2
  list.append(kq)

n1 = [1/list[i] for i in range(0, n)]

#cau k
p = [0]
for i in range(1, n):
  pi = i/(i + 1)
  p.append(pi)

#cau l
list_az = [] 
for i in range(ord('a'), ord('z') + 1):
  list_az.append(chr(i))

#cau m
list_AZ = []
for i in range(ord('A'), ord('Z') + 1):
  list_AZ.append(chr(i))

print("-cau a:", b)
print("Vecto b:", np.array(b))

print("-cau b:", c)
print("Vecto c:", np.array(c))

print("-cau c:", x)
print("Vecto x:", np.array(x))

print("-cau d:", y)
print("Vecto y:", np.array(y))

print("-cau e:", z)
print("Vecto z:", np.array(z))

print("-cau f:", w)
print("Vecto w:", np.array(w))

print("-cau g:", d)
print("Vecto d:", np.array(d))

print("-cau h:", e)
print("Vecto e:", np.array(e))

print("-cau i:", a)
print("Vecto a:", np.array(a))

print("-cau j:", n1)
print("Vecto n:", np.array(n))

print("-cau k:", p)
print("Vecto p:", np.array(p))

print("-cau l:", list_az)
print("Vecto o:", np.array(list_az))

print("-cau m:", list_AZ)
print("Vecto s:", np.array(list_AZ))