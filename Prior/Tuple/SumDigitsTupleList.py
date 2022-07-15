# Sort tuple by taking sum of digits. Tuple with min sum should be at first index.
list = [(3,4,6,723),(1,2),(134,234,34)]
# 723 % 10 = 3
tempList = []

# tuple to list
for tuple in list:
    for value in tuple:
        tempList.append(value)

print(tempList)

# split items > 10 in list
splitList = [int(d) for d in ''.join(str(x) for x in tempList)]
# '' + 2 = '2'
print(splitList)

# sum of items in list
print(sum(splitList))

