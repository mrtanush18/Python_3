# import itertools 

# x = []

# set2 = {10,20,30,40}
# n2 = 3

# x = list(itertools.combinations(set2,n2))

# print(x)

# o/p : [(40, 10, 20), (40, 10, 30), (40, 20, 30), (10, 20, 30)]

# hw: o/p without module iterator tools after sets is over

# TRIED USING BELOW METHOD, NOT WORKING AS VALUE IN INDEX OF SET KEEPS CHANGING

set2 = {10,20,30,40,50,60}

y = enumerate(set2)

# print(list(y))

for index,value in enumerate(set2,1):
    print(value,index)
    # not possible : print(set[index])

# o/p :
# 40 0
# 10 1
# 20 2
# 30 3