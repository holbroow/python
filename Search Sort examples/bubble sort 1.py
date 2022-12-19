## Bubble Sort

def BubbleSort(myList):
    for endPoint in range (len(myList)-1):
        for IndexPos in range (len(myList)-1):
            if myList[IndexPos] > myList[IndexPos+1]:
                myList[IndexPos], myList[IndexPos+1] = myList[IndexPos]
        print(myList)


WillsList = [8,3,5,4,25,2334,6,8,9,100]


BubbleSort(WillsList)
