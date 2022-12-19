def highest_lowest():
    file = open("scores.csv", "r")

    highest = 0
    lowest = 100

    for line in file:
        try:
            line = int(line.strip())

            if int(line) >= highest:
                highest = int(line)
                
            
            if int(line) <= lowest:
                lowest = int(line)
                

            
        except ValueError:
            print("Value is not an integer!")

    print("Highest value is", highest)
    print("Lowest value is", lowest)

    file.close()



highest_lowest()
