
myISBN = [9780007348695, 9780007547999, 9780007580910, 9780008270360, 9780008284220, 9780008300630, 9780062388865, 9780321573513, 9780747581086, 9780747591061, 9781408855669, 9781408855676, 9781408855690, 9781408855928, 9781551922737, 9781743607886, 9781798662915, 9781912286478, 9781980411680, 9781982074647] 


number_to_find = 9780007547999



def findValue(myISBN, number_to_find):
	low = 0
	high = len(listnumbers - 1

        while low <= high:
		middle = low + (high - low) // 2

		if numbers[middle] == number_to_find:
			return middle
		elif numbers[middle] < number_to_find:
			low = middle + 1
		else:
			high = middle - 1
	return -1


final = findValue(numbers, number_to_find)

if final == -1:
	print("This item was not found in the list.")
else:
	print("The number " + str(number_to_find) + " was found at index position " + str(final) + ".")
