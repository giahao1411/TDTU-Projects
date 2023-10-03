import itertools


def combos(items, n):
    return {' '.join(combo) for combo in itertools.combinations(items, n)}


urn = {'0', '1', '2', '3', '4', '5'}


threeDigitNumbers = list(itertools.combinations(urn, 3))
print(threeDigitNumbers)

print()
fourDigitNumbers = list(itertools.permutations(urn, 4))
print(fourDigitNumbers)
