
list0 = ["I", "like","python", "programming"]

list_index = [0,1,"2",3]

for i in range(len(list_index)):
    try:
        print(list0[list_index[i]])
    except TypeError:
        print('Value of i must be integer not string')

# o/p:
# I
# like
# Value of i must be integer not string