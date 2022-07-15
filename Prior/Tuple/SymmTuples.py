# Print symmetric tuples 
# ex. o/p : {(6,7),(2,3)}

list = [(6,7),(2,3),(7,6),(3,2),(1,2)] 
list2 = []
symm = []

# create list2 with reversed tuples from list
for tuple in list:
    new_tup = tuple[::-1]
    list2.append(new_tup)
# compare both list of tuples
    for tup in list2:
        if tuple == tup:
            symm.append(tuple)
        else:
            continue

# print(list2)
print(symm)


# o/p : [(7, 6), (3, 2), (6, 7), (2, 3)]