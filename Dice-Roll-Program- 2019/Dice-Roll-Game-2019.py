### 447 Lines of Code

## I NEED TO IMPORT RANDOM FOR THE RANDOM PICK BETWEEN 1-6 WHEN ROLLING THE DIE ##
## I NEED TO IMPORT TIME FOR ASTHETIC PAUSES BETWEEN CERTAIN LINES

import random
import time

from datetime import datetime

############################################################

file = open("scoreboard.txt","a")

############################################################

def login_p1():
    print("========================")
    print("========Player 1========")
    print("========================")
    print()
    login = False
    while login == False:
        print("Please enter your details below: ")
        details = [['will', 'chungus'], ['alex', 'burton'], ['hello', 'world']]
        P1name = input("Please enter your username: ")
        for each in details:
            if each[0] == P1name:
                P1pass = input("Please enter your password: ")
                for each in details:
                    if each[1] == P1pass:
                        return P1name
                        login = True
                        print("")
                        print("Authenticated!")
                        print("")
                        break
                    else:
                        P1pass = input("Password not correct... Please press enter...")
                        break

def login_p2():
    time.sleep(0.5)
    print("========================")
    print("========Player 2========")
    print("========================")
    print()
    login = False
    while login == False:
        print("Please enter your details below: ")
        details = [['alex', 'chungus'], ['alex', 'burton'], ['hello', 'world']]
        P2name = input("Please enter your username: ")
        for each in details:
            if each[0] == P2name:
                P2pass = input("Please enter your password: ")
                for each in details:
                    if each[1] == P2pass:
                        return P2name
                        login = True
                        print("")
                        print("Authenticated!")
                        print("")
                        break
                    else:
                        P2pass = input("Password not correct... Please press enter...")
                        break

############################################################

##WE NEED TO SET THE OVERALL SCORE, NOT THE PER ROUND SCORE, AS 0 IN ORDER TO GIVE IT A VALUE AND DISPLAY IT AT THE END OF EACH ROUND

p1_game_score = 0
p2_game_score = 0

############################################################

dice_total_p1 = 0
dice_total_p2 = 0

############################################################

def dice_roll_p1():
    p1_overall_score = 0
    time.sleep(1) # SLEEP FOR 1 SECOND
    dice1 = random.randint(1,6)
    print("")
    print("Your first roll is: ", dice1)
    time.sleep(1) # SLEEP FOR 1 SECOND
    dice2 = random.randint(1,6)
    print("Your second roll is: ", dice2)
    if dice1 == dice2:
        dice3 = random.randint(1,6)
        time.sleep(1) # SLEEP FOR 1 SECOND
        print("Your third roll is: ", dice3)
        print("")
        dice_total_p1 = dice1 + dice2 + dice3
        time.sleep(1) # SLEEP FOR 1 SECOND
        print("Your sub total for this ROUND is: ", dice_total_p1)
        print("")
        p1_overall_score = p1_overall_score + dice_total_p1
        if dice_total_p1 %2 == 0:                    ## Program that determines wether the score is even or odd and 
            dice_total_p1 = dice_total_p1 + 10                  ## based on that, subtacts or adds score.
            print("Your sub score is even, you have been awarded 10 points!,Your new score for this current round is", dice_total_p1)
            p1_overall_score = p1_overall_score + dice_total_p1
            return p1_overall_score
            return dice_total_p1 ## return in order to count up at the end of the program
        else:
            dice_total_p1 = dice_total_p1 - 5
            print("Your sub score is odd, you have been deducted 5 points!, Your new score for this current round is", dice_total_p1)
            if dice_total_p1 < 0:
                print("The score has fallen below 0, therefore you have been increased to the minimum score of 0.")
                dice_total_p1 = 0
                p1_overall_score = p1_overall_score + dice_total_p1
                return p1_overall_score
                return dice_total_p1 ## return in order to count up at the end of the program
            else:
                p1_overall_score = p1_overall_score + dice_total_p1
                return p1_overall_score
                return dice_total_p1 ## return in order to count up at the end of the program
    else:
        dice_total_p1 = dice1 + dice2
        time.sleep(1) # SLEEP FOR 1 SECOND
        print("Your sub total for this ROUND is: ", dice_total_p1)
        print("")
        if dice_total_p1 %2 == 0:                    ## Program that determines wether the score is even or odd and 
            dice_total_p1 = dice_total_p1 + 10       ## based on that, subtacts or adds score.
            print("Your sub score is even, you have been awarded 10 points!, Your new score for this current round is", dice_total_p1)
            p1_overall_score = p1_overall_score + dice_total_p1
            return p1_overall_score
            return dice_total_p1 ## return in order to count up at the end of the program
        else:
            dice_total_p1 = dice_total_p1 - 5
            print("Your sub score is odd, you have been deducted 5 points!, Your new score for this current round is", dice_total_p1)
            if dice_total_p1 < 0:
                print("The score has fallen below 0, therefore you have been increased to the minimum score of 0.")
                dice_total_p1 = 0
                p1_overall_score = p1_overall_score + dice_total_p1
                return p1_overall_score
                return dice_total_p1 ## return in order to count up at the end of the program
            else:
                p1_overall_score = p1_overall_score + dice_total_p1
                return p1_overall_score
                return dice_total_p1 ## return in order to count up at the end of the program


def dice_roll_p2():
    p2_overall_score = 0
    time.sleep(1) # SLEEP FOR 1 SECOND
    dice1 = random.randint(1,6)
    print("")
    print("Your first roll is: ", dice1)
    time.sleep(1) # SLEEP FOR 1 SECOND
    dice2 = random.randint(1,6)
    print("Your second roll is: ", dice2)
    if dice1 == dice2:
        dice3 = random.randint(1,6)
        time.sleep(1) # SLEEP FOR 1 SECOND
        print("Your third roll is: ", dice3)
        print("")
        dice_total_p2 = dice1 + dice2 + dice3
        time.sleep(1) # SLEEP FOR 1 SECOND
        print("Your sub total for this ROUND is: ", dice_total_p2)
        print("")
        if dice_total_p2 %2 == 0:                    ## Program that determines wether the score is even or odd and 
            dice_total_p2 = dice_total_p2 + 10       ## based on that, subtacts or adds score.
            print("Your sub score is even, you have been awarded 10 points!, Your new score for this current round is", dice_total_p2)
            p2_overall_score = p2_overall_score + dice_total_p2
            return p2_overall_score
            return dice_total_p2 ## return in order to count up at the end of the program
        else:
            dice_total_p2 = dice_total_p2 - 5
            print("Your sub score is odd, you have been deducted 5 points!, Your new score for this current round is", dice_total_p2)
            if dice_total_p2 < 0:
                print("The score has fallen below 0, therefore you have been increased to the minimum score of 0.")
                dice_total_p2 = 0
                p2_overall_score = p2_overall_score + dice_total_p2
                return p2_overall_score
                return dice_total_p2 ## return in order to count up at the end of the program
            else:
                p2_overall_score = p2_overall_score + dice_total_p2
                return p2_overall_score
                return dice_total_p2 ## return in order to count up at the end of the program
        
    else:
        dice_total_p2 = dice1 + dice2
        time.sleep(1) # SLEEP FOR 1 SECOND
        print("Your sub total for this ROUND is: ", dice_total_p2)
        print("")
        if dice_total_p2 %2 == 0:                    ## Program that determines wether the score is even or odd and 
            dice_total_p2 = dice_total_p2 + 10                  ## based on that, subtacts or adds score.
            print("Your sub score is even, you have been awarded 10 points!, Your new score for this current round is", dice_total_p2)
            p2_overall_score = p2_overall_score + dice_total_p2
            return p2_overall_score
            return dice_total_p2 ## return in order to count up at the end of the program
        else:
            dice_total_p2 = dice_total_p2 - 5
            print("Your sub score is odd, you have been deducted 5 points!, Your new score for this current round is", dice_total_p2)
            if dice_total_p2 < 0:
                print("The score has fallen below 0, therefore you have been increased to the minimum score of 0.")
                dice_total_p2 = 0
                p2_overall_score = p2_overall_score + dice_total_p2
                return p2_overall_score
                return dice_total_p2 ## return in order to count up at the end of the program
            else:
                p2_overall_score = p2_overall_score + dice_total_p2
                return p2_overall_score
                return dice_total_p2 ## return in order to count up at the end of the program

############################################################

print("=================================")
print("--------------RULES--------------")
print("=================================")
print("")

print("• Two players roll two 6-sided dice each and get points depending on what they roll.")
print("")
print("• There are 5 rounds in a game. In each round, each player rolls the two dice.")
print("")
print("• If in a round a player rolls a double, they will be awarded a third roll.")
print("")
print("• The points rolled on each player’s dice are added to their score at the end of every round.")
print("")
print("• If the total is an even number, an additional 10 points are added to their score.")
print("")
print("• If the total is an odd number, 5 points are subtracted from their score.")
print("")
print("• The score of a player cannot go below 0 at any point. The score will be reset to 0 if it falls below that point.")
print("")
print("• The person with the highest score at the end of the 5 rounds wins.")
print("")
print("• If both players have the same score at the end of the 5 rounds, they each roll 1 die and whoever gets the highest score wins (this repeats until someone wins)")
print("")
      
############################################################

P1name = login_p1()
print(P1name, "logged in!")
P2name = login_p2()
print(P2name, "logged in!")

print("")
time.sleep(0.75)
print("===================================")
print("--------------ROUND 1--------------")
print("===================================")
print("")
### STATES THE ROUND NUMBER FOR PLAYERS

print("--------------PLAYER 1--------------")
print("")

player_prompt = input("Please press Enter to roll the dice")
if player_prompt == "":
    dice_total_p1 = dice_roll_p1()
    p1_game_score = p1_game_score + dice_total_p1
    print("Overall score is currently: ", p1_game_score)


print("--------------PLAYER 2--------------")
print("")

player_prompt = input("Please press Enter to roll the dice")
if player_prompt == "":
    dice_total_p2 = dice_roll_p2()
    p2_game_score = p2_game_score + dice_total_p2
    print("Overall score is currently: ", p2_game_score)


############################################################


print("===================================")
print("--------------ROUND 2--------------")
print("===================================")
print("")
### STATES THE ROUND NUMBER FOR PLAYERS

print("--------------PLAYER 1--------------")
print("")

player_prompt = input("Please press Enter to roll the dice")
if player_prompt == "":
    dice_total_p1 = dice_roll_p1()
    p1_game_score = p1_game_score + dice_total_p1
    print("Overall score is currently: ", p1_game_score)

print("--------------PLAYER 2--------------")
print("")

player_prompt = input("Please press Enter to roll the dice")
if player_prompt == "":
    dice_total_p2 = dice_roll_p2()
    p2_game_score = p2_game_score + dice_total_p2
    print("Overall score is currently: ", p2_game_score)

############################################################

print("===================================")
print("--------------ROUND 3--------------")
print("===================================")
print("")
### STATES THE ROUND NUMBER FOR PLAYERS

print("--------------PLAYER 1--------------")
print("")

player_prompt = input("Please press Enter to roll the dice")
if player_prompt == "":
    dice_total_p1 = dice_roll_p1()
    p1_game_score = p1_game_score + dice_total_p1
    print("Overall score is currently: ", p1_game_score)
print("--------------PLAYER 2--------------")
print("")

player_prompt = input("Please press Enter to roll the dice")
if player_prompt == "":
    dice_total_p2 = dice_roll_p2()
    p2_game_score = p2_game_score + dice_total_p2
    print("Overall score is currently: ", p2_game_score)

############################################################

print("===================================")
print("--------------ROUND 4--------------")
print("===================================")
print("")
### STATES THE ROUND NUMBER FOR PLAYERS

print("--------------PLAYER 1--------------")
print("")

player_prompt = input("Please press Enter to roll the dice")
if player_prompt == "":
    dice_total_p1 = dice_roll_p1()
    p1_game_score = p1_game_score + dice_total_p1
    print("Overall score is currently: ", p1_game_score)

print("--------------PLAYER 2--------------")
print("")

player_prompt = input("Please press Enter to roll the dice")
if player_prompt == "":
    dice_total_p2 = dice_roll_p2()
    p2_game_score = p2_game_score + dice_total_p2
    print("Overall score is currently: ", p2_game_score)

############################################################

print("===================================")
print("--------------ROUND 5--------------")
print("===================================")
print("")
### STATES THE ROUND NUMBER FOR PLAYERS

print("--------------PLAYER 1--------------")
print("")

player_prompt = input("Please press Enter to roll the dice")
if player_prompt == "":
    dice_total_p1 = dice_roll_p1()
    p1_game_score = p1_game_score + dice_total_p1
    print("Overall score is currently: ", p1_game_score)

print("--------------PLAYER 2--------------")
print("")

player_prompt = input("Please press Enter to roll the dice")
if player_prompt == "":
    dice_total_p2 = dice_roll_p2()
    p2_game_score = p2_game_score + dice_total_p2
    print("Overall score is currently: ", p2_game_score)


############################################################

tie_broken = False
while tie_broken == False:
    if p1_game_score == p2_game_score:
        print("================================")
        print("-----------TIEBREAKER-----------")
        print("================================")
        print("")
        print("--------------PLAYER 1--------------")
        print("")
        player_prompt = input("Please press Enter to roll the dice")
        if player_prompt == "":
            dice_total_p1 = dice_roll_p1()
            p1_game_score = p1_game_score + dice_total_p1
            print("Overall score is currently: ", p1_game_score)
        print("--------------PLAYER 2--------------")
        print("")
        player_prompt = input("Please press Enter to roll the dice")
        if player_prompt == "":
            dice_total_p2 = dice_roll_p2()
            p2_game_score = p2_game_score + dice_total_p2
            print("Overall score is currently: ", p2_game_score)
        if p1_game_score != p2_game_score:
            tie_broken = True
    else:
        print("============================================")
        print("-----------TIE IS ALREADY BROKEN!-----------")
        print("============================================")
        break
    
############################################################

print("---------------------------------------------------")

time.sleep(1) # SLEEP FOR 1 SECOND
print("Player 1 total for this GAME is: ", p1_game_score)


time.sleep(1) # SLEEP FOR 1 SECOND
print("Player 2 total for this GAME is: ", p2_game_score)

if p1_game_score > p2_game_score:
    print("")
    time.sleep(0.5)
    print("====================================")
    print("-----------PLAYER 1 WINS!-----------")
    print("====================================")
    file.write(str("\n"))
    file.write(str(datetime.date(datetime.now())))##It prints the date here...
    file.write(str("\n"))
    file.write(str(P1name))
    file.write(str(", "))
    file.write(str(p1_game_score))
    file.write(str("\n"))
    print("")
    print("Your score has been added to the scoreboard, Thank you for playing.")

elif p1_game_score < p2_game_score:
    print("")
    time.sleep(0.5)
    print("====================================")
    print("-----------PLAYER 2 WINS!-----------")
    print("====================================")
    file.write(str("\n"))
    file.write(str(datetime.date(datetime.now())))##It prints the date here...
    file.write(str("\n"))
    file.write(str(P2name))
    file.write(str(", "))
    file.write(str(p2_game_score))
    file.write(str("\n"))
    print("")
    print("Your score has been added to the scoreboard, Thank you for playing.")
        
file.close()
