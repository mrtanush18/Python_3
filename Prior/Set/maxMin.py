set1 = {1,2,3,-1,4,5,6}

max = 0
min = 0

for item in set1:
    if item > max:
        max = item

print("Max: ",max)

# converting set to list to find min
list1 = list(set1)
min = list1[0]

for item in list1:
    if item < min:
        min = item

print("Min: ",min)