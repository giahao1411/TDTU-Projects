import random


def dice():
    return random.randint(1, 6), random.randint(1, 6)


def dice_a(n):
    count = 0
    for i in range(n):
        dice1, dice2 = dice()
        if dice1 == dice2:
            count += 1
    return count


def dice_b(n):
    count = 0
    for i in range(n):
        dice1, dice2 = dice()
        if dice1 != dice2:
            count += 1
    return count


def dice_c(n):
    count = 0
    for i in range(n):
        dice1, dice2 = dice()
        if dice1 % 2 == 0 and dice2 % 2 == 0:
            count += 1
    return count


def dice_d(n):
    count = 0
    for i in range(n):
        dice1, dice2 = dice()
        if dice1 % 2 != 0 and dice2 % 2 != 0:
            count += 1
    return count


def dice_e(n):
    count = 0
    for i in range(n):
        dice1, dice2 = dice()
        if (dice1 + dice2) % 2 != 0:
            count += 1
    return count


def dice_f(n):
    count = 0
    for i in range(n):
        dice1, dice2 = dice()
        if dice1 == 6 and dice2 == 6:
            count += 1
    return count


def dice_g(n):
    count = 0
    for i in range(n):
        dice1, dice2 = dice()
        if (dice1 + dice2) > 10:
            count += 1
    return count


n = 10000

print(dice_a(n)/n)
print(dice_b(n)/n)
print(dice_c(n)/n)
print(dice_d(n)/n)
print(dice_e(n)/n)
print(dice_f(n)/n)
print(dice_g(n)/n)
