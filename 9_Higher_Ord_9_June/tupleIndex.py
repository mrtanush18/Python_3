num = [10,20,30,40,50,60,70,80]
char = ['A','B','C','D','E','F','G','H']
list2 = []
x = ()

def tupleIndex(a,b):
    list2.append(a)
    list2.append(b)
    x = tuple(list2)
    list2.clear()
    return x

list1 = map(tupleIndex, num, char)

print(list(list1))

# o/p : [(10, 'A'), (20, 'B'), (30, 'C'), (40, 'D'), (50, 'E'), (60, 'F'), (70, 'G'), (80, 'H')]