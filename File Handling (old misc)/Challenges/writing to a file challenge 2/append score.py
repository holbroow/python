import datetime

score_entered = input("Please enter your latest score: ")

currenttime = datetime.datetime.now() 
timestamp = currenttime.strftime("%d-%m-%Y %H:%M:%S")



file = open("scores.txt", "a")


file.write(score_entered + "recorded at: " + timestamp)

