import random

#Both dices are even -> (3C1+3C1)/(6C1*6C1) = 1/6
def simulator_dice1(n):
    count = 0
    for i in range(n):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        if dice1 % 2 == 0 and dice2 % 2 == 0:
            count += 1
    return count

#1 odd and the other is even -> (3C1+3C1)/(6C1*6C1) = 1/6
def simulator_dice2(n):
    count = 0
    for i in range(n):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        if (dice1 + dice2) % 2 != 0:
            count += 1
    return count

#Both dices are the same -> (6C1+1C1)/(6C1*6C1) = 7/36
def simulator_dice3(n):
    count = 0
    for i in range(n):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        if dice1 == dice2:
            count += 1
    return count

#One gives 1 and the other gives 6 -> (1C1+1C1/6C1*6C1) = 1/18
def simulator_dice4(n):
    count = 0
    for i in range(n):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        if (dice1 == 1 and dice2 == 6) or (dice2 == 1 and dice1 == 6):
            count += 1
    return count

#6-1 6-2 6-3 6-4 6-5 6-6 5-2 5-3 5-4 5-5 5-6 4-3 4-4 4-5 4-6 3-4 3-5 3-6 2-5 2-6 1-6 -> larger than 6 -> ? sample spaces
#1-2 1-3 1-4 1-5 2-1 2-2 2-3 2-4 3-1 3-2 3-3 4-1 4-2 5-1 -> smaller than 6 - > 14 sample spaces
#Sum 2 dices are larger than 6 -> 1 - 14/(6C1*6C1) = 11/18
def simulator_dice5(n):
    count = 0
    for i in range(n):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        if (dice1 + dice2) > 6:
            count += 1
    return count

n = 1000
print("Both dices are even :", simulator_dice1(n)/n)
print("One odd and one even: ", simulator_dice2(n)/n)
print("Both dices are the same: ", simulator_dice3(n)/n)
print("One gives 1 and one gives 6: ", simulator_dice4(n)/n)
print("Sum 2 dices are larger than 6: ", simulator_dice5(n)/n)