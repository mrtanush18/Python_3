list0 = [2,3,4,7,8]

def reverseList(list1):
    if len(list1) == 0:
        return [] 
    return [list1[-1]] + reverseList(list1[:-1]) # [:-1] means exclude last element
    # return [list1[len(list1)-1]] + reverseList(list1[:len(list1)-1])

print(reverseList(list0))

# o/p : [8, 7, 4, 3, 2]