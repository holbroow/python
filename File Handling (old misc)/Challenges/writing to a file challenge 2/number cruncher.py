
file = open("number_cruncher.txt", "w")

valid = False

while valid == False:
    
    choice = input("Please choose between + / * and -:  ")
    
    if choice == "+":
        num1 = int(input("Please enter your first number: "))
        num2 = int(input("Please enter your second number: "))
        summary = (num1 + num2)
        print("Your answer is: ", summary)

        string = str(summary)
        file.write(string)
        file.close()
        
        valid = True
        
    elif choice == "/":
        num1 = int(input("Please enter your first number: "))
        num2 = int(input("Please enter your second number: "))
        summary = (num1 / num2)
        print("Your answer is: ", summary)
        
        string = str(summary)
        file.write(string)
        file.close()
        
        valid = True
        
    elif choice == "*":
        num1 = int(input("Please enter your first number: "))
        num2 = int(input("Please enter your second number: "))
        summary = (num1 * num2)
        print("Your answer is: ", summary)
        
        string = str(summary)
        file.write(string)
        file.close()
        
        valid = True
        
    elif choice == "-":
        num1 = int(input("Please enter your first number: "))
        num2 = int(input("Please enter your second number: "))
        summary = (num1 - num2)
        print("Your answer is: ", summary)
        
        string = str(summary)
        file.write(string)
        file.close()
        
        valid = True
        
    else:
        print("That value is not valid! Please try again.")
        print("")

        file.close()
        
        valid = False

file = open("number_cruncher.txt", "r")

result = file.read()
file.close()

print("Read from file: ", result)
