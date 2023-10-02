from itertools import combinations_with_replacement

suits = ['♠', '♣', '♦', '♥']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

A1 = ["".join(combination) for combination in combinations_with_replacement(ranks, 3) if combination.count('K') in [1, 2]]

print(A1)
