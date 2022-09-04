# replace 2 in list by 10 and change abc into abcd and return them all as one tuple

ogTuple = ('abc', 4.0, 3, [1,2,3])

for item in ogTuple:
    if(type(item) == list):  # chk if tuple item is list
        for i in range(len(item)):  # iterate in list and modify value
            if item[i] == 2:    
                item[i] = 10
# print(ogTuple)

for item in ogTuple:  
    if(type(item) == list):  
        newTuple = tuple(item) # convert list item in tuple to a tuple

# print(newTuple)

itemsList = []
for item in ogTuple:  
    if(type(item) != list):  
        itemsList.append(item)

for i in range(len(itemsList)): # In list, abc --> abcd
    if itemsList[i] == 'abc':
        itemsList[i] = 'abcd'

newerTuple = tuple(itemsList)

# print(newerTuple)

finalTuple = newerTuple + newTuple 

print(finalTuple)

# o/p : ('abcd', 4.0, 3, 1, 10, 3)