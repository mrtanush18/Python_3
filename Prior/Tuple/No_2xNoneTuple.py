# Print all tuples in list excluding tuple with 2 'none'
list = [('none',2),('none','none'),(3,4),(5,2),('none',)]
list2 = []

for tuple in list:
    if tuple != ('none','none'):
        list2.append(tuple)

print(list2)