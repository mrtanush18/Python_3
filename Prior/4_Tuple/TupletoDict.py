# Desired o/p : {5:3,2:2,1:2,7:1}

tuple = (5,1,5,2,5,2,7,1)

dict = {}

for value in tuple:
    if value not in dict:
        dict[value] = 1
    else:
        dict[value] = dict[value] + 1

print(dict)

# o/p : {5: 3, 1: 2, 2: 2, 7: 1}