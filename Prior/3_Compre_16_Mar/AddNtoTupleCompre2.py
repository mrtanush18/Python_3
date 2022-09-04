# want o/p : [(11, 13, 14), (12, 14, 16), (13, 18, 11)], simplify "AddNtoTupleCompre.py"

list = [(1,3,4),(2,4,6),(3,8,1)]

sumList = [sum := 10+tuple[i] for tuple in list for i in range(len(tuple))]
# sumList = [sum := 10 + tuple[i] for tuple in list tuple(for i in range(len(tuple)))]
# print(sumList)

print(sumList)