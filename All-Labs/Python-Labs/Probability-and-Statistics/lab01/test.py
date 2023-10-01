import itertools

E = {'a', 'b', 'c', 'd'}
k = 3
n = len(E)

permute = list(itertools.permutations(E, k))
print("%i-permutations of %s: " %(k, E))

for i in permute:
    print(i)
print("Size = ", "%i!/(%i-%i)! = " %(n, n, k), len(permute))

print("----------------------------------------")

combi = list(itertools.combinations(E, k))

for i in combi:
    print(i)

print("Size = ", "%i!/(%i!(%i-%i)!) = " %(n, k, n, k), len(combi))
