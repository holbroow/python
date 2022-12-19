file = open("numbers.txt","r")

num = 0


for line in file:
    num = num + int(line)


print(num)
