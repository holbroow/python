
#Step 1
passwords = [   
    [], 
    [], 
    []
    ]


#Step 2
passwords[0].append ("Raspbian") 


#Step 3
passwords[1].append ("pi") 
passwords[2].append ("raspberry") 


#Step 4
print(passwords)



###   Name = 0   Username = 1   Password = 2

#Iteratively populate the list
valid = True

try:
    while valid == True:
        choice = input("Would you like to enter a new set of details? Y/N: ")

        if choice == 'Y':
            passwords[0].append (input("Please enter a name: "))
            passwords[1].append (input("Please enter a username: "))
            passwords[2].append (input("Please enter a password: "))

            valid = False
            break
        
        elif choice == 'No':
            print("Okay. Goodbye!")
            valid = False
            break

        else:
            valid = True

except:
    print("That isn't a valid value! Please try again.")


## This is to test that the code functions in the correct manner. ##
print(passwords)



########access an account username and password (TASK)
choice2 = input("Please enter the account name: ")

if choice2 in password[0]:
    print(passwords)