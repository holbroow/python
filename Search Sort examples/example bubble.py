## bubble sort

def BubbleSort(myList):
    for endPoint in range(len(myList)-1):
        for IndexPos in range(len(myList)-1):
            if myList[IndexPos] > myList[IndexPos+1]:
                myList[IndexPos], myList[IndexPos+1] = myList[IndexPos+1] , myList[IndexPos]
    print(myList)

TheList = [5,2,3,8,7,4]

BubbleSort(TheList)

##### had help with this
