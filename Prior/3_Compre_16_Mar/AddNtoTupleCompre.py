# import time
# begin = time.time()

list = [(1,3,4),(2,4,6),(3,8,1)]

list2 = []                             # global variable

def add10toTuple(tuple):
    sum = 0                            # imp
    tup = ()                           # local variable

    for i in range(len(tuple)):
        sum = 10 + tuple[i]
        tup = tup + (sum,)
    list2.append(tup)                  # imp      

    # end = time.time()
    # print("Time taken: ",end-begin)

sumList = [add10toTuple(tuple) for tuple in list]

print(list2)

# o/p : [(11, 13, 14), (12, 14, 16), (13, 18, 11)]


