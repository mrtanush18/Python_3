list = [(1,),(2,4),(3,8,1),(1,2,3,4),(2,)]
list2 = []

size = int(input('Enter size of tuple in list: '))

for tuple in list:
    if(len(tuple) != size):
        list2.append(tuple)

print(list2)


