import random
###
print("--------------ROUND 1--------------")
###

print("PLAYER 1")
print("")

dice_total_p1 = 0
dice1 = random.randint(1,6)
print("Your first roll is: ", dice1)
dice2 = random.randint(1,6)
print("Your second roll is: ", dice2)
if dice1 == dice2:
    dice3 = random.randint(1,6)
    print("Your third roll is: ", dice3)
    print("")
    dice_total_p1 = dice1 + dice2 + dice3
    print("Your total for this round is: ", dice_total_p1)
    print("")
else:
    dice_total_p1 = dice1 + dice2
    print("Your total for this round is: ", dice_total_p1)
    print("")

print("PLAYER 2")
print("")

dice_total_p2 = 0
dice1 = random.randint(1,6)
print("Your first roll is: ", dice1)
dice2 = random.randint(1,6)
print("Your second roll is: ", dice2)
if dice1 == dice2:
    dice3 = random.randint(1,6)
    print("Your third roll is: ", dice3)
    print("")
    dice_total_p2 = dice1 + dice2 + dice3
    print("Your total for this round is: ", dice_total_p2)
    print("")
    
else:
    dice_total_p2 = dice1 + dice2
    print("Your total for this round is: ", dice_total_p2)
    print("")



print("Player 1 total for this round is: ", dice_total_p1)
print("")
print("Player 2 total for this round is: ", dice_total_p2)

###
print("--------------ROUND 2--------------")
###

print("PLAYER 1")
print("")


dice1 = random.randint(1,6)
print("Your first roll is: ", dice1)
dice2 = random.randint(1,6)
print("Your second roll is: ", dice2)
if dice1 == dice2:
    dice3 = random.randint(1,6)
    print("Your third roll is: ", dice3)
    print("")
    dice_total_p1 = dice1 + dice2 + dice3
    print("Your total for this round is: ", dice_total_p1)
    print("")
else:
    dice_total_p1 = dice1 + dice2
    print("Your total for this round is: ", dice_total_p1)
    print("")

print("PLAYER 2")
print("")


dice1 = random.randint(1,6)
print("Your first roll is: ", dice1)
dice2 = random.randint(1,6)
print("Your second roll is: ", dice2)
if dice1 == dice2:
    dice3 = random.randint(1,6)
    print("Your third roll is: ", dice3)
    print("")
    dice_total_p2 = dice1 + dice2 + dice3
    print("Your total for this round is: ", dice_total_p2)
    print("")
    
else:
    dice_total_p2 = dice1 + dice2
    print("Your total for this round is: ", dice_total_p2)
    print("")



print("Player 1 total for this round is: ", dice_total_p1)
print("")
print("Player 2 total for this round is: ", dice_total_p2)


### please add code to keep track of overall score at the end of every round
