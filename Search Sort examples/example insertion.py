## Insertion sort

def InsertionSort(myList): 

    for i in range(1,len(myList)):

        currentValue = myList[i] # Gets the current value we are comparing against the sorted list

        while myList[i - 1] > currentValue and i > 0:
            myList[i] = myList[i - 1] # Moves the sorted list up an index
            i = i - 1
        
        myList[i] = currentValue # Insert the current value into the correct index

    return(myList)            

theList = [4,2,3,6,5,1]

print(InsertionSort(theList)) # argument theList is passed to InsertionSort function

