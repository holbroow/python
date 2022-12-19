import random


def dice_roll():
    score = 0
    dice1 = random.randint(1,6)
    print("Your first roll is: ", dice1)
    dice2 = random.randint(1,6)
    print("Your second roll is: ", dice2)
    if dice1 == dice2:
        dice3 = random.randint(1,6)
        print("Your third roll is: ", dice3)
        dice_total = dice1 + dice2 + dice3
        print("Your total for this round is: ", dice_total)
    else:
        dice_total = dice1 + dice2
        print("Your total for this round is: ", dice_total)

dice_roll()
