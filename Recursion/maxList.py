# find max element in list using recursion
list0 = [4,3,23,2,1]

def maxList(list1):
    if list1 == []:
        return
    if len(list1) == 1:
        return list1[0]
    else:
        return max(maxList(list1[1:]),list1[0])

print(maxList(list0))

# o/p : 23