import itertools

A = {'1', '2', '3', '4', '5'}
k = 3 
n = len(A)

res = list(itertools.permutations(A, k))

print("%i permutations of %s: " %(k, A))

for i in res:
    print(i)

print("Size = ", "%i!/(%i-%i)! = " %(n, n, k), len(res))
