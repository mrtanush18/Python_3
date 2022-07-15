# Sort tuple by taking sum of digits. Tuple with min sum should be at first index.
# even 723,134,234,34's sum should be calculated

list = [(3,4,6,723),(1,2),(134,234,34)]
dict = {}

# sort list
for tuple in list:
    sum = 0
    for i in range(len(tuple)):
        sum = sum + tuple[i]
    dict[tuple] = sum
# print(dict)

sortedValues = sorted(dict.items(), key=lambda x: x[1])
print(sortedValues)

