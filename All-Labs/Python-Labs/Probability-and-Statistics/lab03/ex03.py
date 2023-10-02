import random
import itertools

suits = ['♠', '♣', '♦', '♥']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

Cards = []

# (a):
for i in ranks:
    for j in suits:
        hand = i + j
        Cards.append(hand)

# print(Cards)

# (b):
B = random.sample(Cards, 3)
print(B)

# (c):
A1 = [s for s in itertools.combinations(B, 3) if sum(
    str(card).count('K') for card in s) in [1, 2]]
print(A1)

# (d):
A2 = [s for s in itertools.combinations(
    B, 3) if any('K' in str(card) for card in s)]
print(A2)

# (e):
sample_space = len(list(itertools.combinations(Cards, 3)))
prob_A1 = len(A1) / sample_space
prob_A2 = len(A2) / sample_space

print("Probability of A1: ", prob_A1)
print("Probability of A2: ", prob_A2)
