nameArray = ['Liliana', 'Will', 'Ben', 'Jake', 'Aubrey', 'Cole', 'Paul', 'Emma']

def linear_search(items, search_item):
    index = -1
    current = 0
    found = False


    while current < len(items) and found == False:

        if items[current] == search_item:
            index = current
            found = True


        current = current +1

    return index


search = input ('Please enter your name for the linear search: ')

search_Found = linear_search(nameArray, search)

print('The city has been found in index number {0}'.format(search_Found))
