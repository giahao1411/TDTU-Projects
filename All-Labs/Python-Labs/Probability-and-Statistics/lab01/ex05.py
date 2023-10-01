import itertools

suits = ['♠', '♣', '♦', '♥']
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

cards = []

#a

for suit in suits:
    for rank in ranks: 
        cards.append((suit, rank))

poker_5 = list(itertools.combinations(cards, 5))

print("a. len of poker 5:", len(poker_5))

#b

three_of_a_kind = []

for hand in poker_5:
    ranks = [card[0] for card in hand]
    unique_ranks = set(ranks)
    if len(unique_ranks) == 3:
        for rank in unique_ranks:
            if ranks.count(rank) == 3:
                three_of_a_kind.append(hand)
                break

print("b. len of three of a kind:", len(three_of_a_kind))
