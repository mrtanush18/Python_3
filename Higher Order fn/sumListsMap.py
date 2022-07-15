list1 = [10,20,30,40,50]
list2 = [1,20,9,56,78]

def sumLists(a,b):
    return a + b

ans = map(sumLists, list1, list2)

print(list(ans))

# o/p : [11, 40, 39, 96, 128]




""" 
ZIP CAN'T BE USED HERE :
result = zip(list1, list2)
print(list(result))
# o/p : [(10, 1), (20, 20), (30, 9), (40, 56), (50, 78)]
"""