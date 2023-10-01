import itertools

def cross(A, B):
    return {a + b for a in A for b in B}

urn = cross('W', '12345678') | cross('B', '123456') | cross('R', '123456789')
print(urn)

#solution for a
U3 = list(itertools.combinations(urn, 3))

for i in U3:
    print(i)

print("Size = " "%i/(%i!(%i-%i)!) = " %(len(urn), 3, len(urn), 3), len(U3))

print("\n")
 
# solution for b
for i in U3:
    # a = i[0][0]
    # b = i[1][0]
    # c = i[2][0]
    # list = {a, b, c}
    # if(len(set(list)) == 3):
    #     print(i)
    if i[0][0] != i[1][0] and i[0][0] != i[2][0]:
        if i[1][0] != i[2][0]:
            print(i)

print("\n")

#solution for c
for i in U3:
    if i[0][0] == 'W' and i[1][0] == 'R':
        print(i)
