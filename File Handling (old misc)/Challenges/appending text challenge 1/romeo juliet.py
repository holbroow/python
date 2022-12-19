file = open("romeojuliet.txt", "r")

fileText = ""
fileText = file.read()

file.close()




usrChoice = str(input("Please enter the character that you want to search for: "))

count = fileText.count(usrChoice)



print ("Letter: ", usrChoice)
print ("Occurences:", count)






file = open("romeojuliet.txt", "a")


countStr = str(count)


file.write ("\n" + "Letter: " + usrChoice + "Occurences:" + countStr)

file.close()
