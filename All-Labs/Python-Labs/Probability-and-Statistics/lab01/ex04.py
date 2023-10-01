import itertools

list_men = ['M1', 'M2', 'M3', 'M4', 'M5', 'M6']
list_women =  ['W1', 'W2', 'W3', 'W4', 'W5', 'W6', 'W7', 'W8', 'W9']

selected_men = list(itertools.combinations(list_men,  3))
selected_women = list(itertools.combinations(list_women, 2))

print("Total sample spaces: ", len(list_men) * len(list_women))

for men in selected_men:
    for women in selected_women:
        print("Men: ", ', '.join(men))
        print("Women: ", ', '.join(women))
        print()

