list = [(3,4,5),(4,5,7),(1,4)]
list2 = []

for tuple in list:
    for value in tuple:
        if value not in list2:
            list2.append(value)

print(list2)
