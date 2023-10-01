import itertools

def cross(A, B):
    return {a + b for a in A for b in B}

urn =  cross('W', '12345678') | cross('B', '123456') | cross('R', '123456789')

print(urn)

U6 = list(itertools.combinations(urn, 6))

print("Solution for a:")
print(len(U6))

print("Solution for b:")

for s in U6:
    print(s)

print("Solution for c:")

for s in U6:
    if s[0][0] == 'R' and s[-1][0] == 'R':
        print(s)

