import random


def dice_roll():
    score = 0
    dice1 = random.randint(1,6)
    print(dice1)
    dice2 = random.randint(1,6)
    print(dice2)
    if dice1 == dice2:
        dice3 = random.randint(1,6)
        print(dice3)
        dice_total = dice1 + dice2 + dice3
        print(dice_total)
    else:
        dice_total = dice1 + dice2
        print(dice_total)

dice_roll()
