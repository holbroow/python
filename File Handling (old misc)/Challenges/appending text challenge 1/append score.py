import datetime

file = open("scores.txt", "a")

score_entered = input("Please enter your latest score: ")

currenttime = datetime.datetime.now() 
timestamp = currenttime.strftime("%d-%m-%Y %H:%M:%S")



file.write("\n" + score_entered + " recorded at: " + timestamp)

file.close()
