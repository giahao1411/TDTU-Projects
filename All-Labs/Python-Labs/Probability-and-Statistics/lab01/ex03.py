import itertools

#EX3
print("EX3")

mathBooks = ['M1', 'M2', 'M3', 'M4']
physicsBooks = ['P1', 'P2', 'P3']
chemistryBooks = ['C1', 'C2']
languageBooks = ['L1']

arrangements = itertools.permutations([mathBooks, physicsBooks, chemistryBooks, languageBooks])

print("Total sample spaces: ", len(list(arrangements)))
      
arrangements = itertools.permutations([mathBooks, physicsBooks, chemistryBooks, languageBooks])

for arrangement in arrangements:
    for group in arrangement:
        for book in group:
            print(book, end=' ')
    print()