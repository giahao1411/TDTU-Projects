#bai 8

import numpy as np

#list char (look up table)
lchar = list(map(chr, range(97 - 32, 123 - 32)))
lchar.append(" ")

#initiate an array A
A = np.array([
    [3, 4, 5],
    [1, 3, 1],
    [1, 1, 2]
])

#initiate 2 encode result
res1 = []
res2 = []

msg1 = list("ATTACK")
msg2 = list(" LINEAR ALGEBRA LABORATORY ")

#encode msg1 
for i in msg1:
  for j in range(0, len(lchar), 1):
    if i == lchar[j]:
      res1.append(j + 4)

encode1 = np.array(res1)
encode1 = encode1.reshape(3, 2)
result1 = np.matmul(A, encode1)
print("ATTACK = ")
print(result1, "\n")

#encode msg2
for i in msg2:
  for j in range(0, len(lchar), 1):
    if i == lchar[j]:
      res2.append(j + 4)

encode2 = np.array(res2)
encode2 = encode2.reshape(3, 9)
result2 = np.matmul(A, encode2)
print("LINEAR ALGEBRA LABORATORY = ")
print(result2)