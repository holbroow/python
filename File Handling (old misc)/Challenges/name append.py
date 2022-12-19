Name1 = input("Please enter name 1: ")
Name2 = input("Please enter name 2: ")
Name3 = input("Please enter name 3: ")
Name4 = input("Please enter name 4: ")


file = open("namelist.txt","w")

file.write(Name1 + "\n")
file.write(Name2 + "\n")
file.write(Name3 + "\n")
file.write(Name4 + "\n")


file.close()
