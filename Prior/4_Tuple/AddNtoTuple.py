# import time
# begin = time.time()

list = [(1,3,4),(2,4,6),(3,8,1)]
tuple1 = ()
list2 = []

for tuples in list:
    length = len(tuples)
    sum = 0
    tuple1 = ()
    for i in range(length):
        sum = tuples[i] + 10
        tuple1 = tuple1 + (sum,)
    list2.append(tuple1)
    
    # end = time.time()
    # print("Time taken: ",end-begin)

print(list2)

# o/p : [(11, 13, 14), (12, 14, 16), (13, 18, 11)]