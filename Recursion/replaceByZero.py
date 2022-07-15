list0 = [10,-20,50,-60]

def replaceByZero(list1, index):
    if index == len(list1):
        return

    if list1[index] < 0:
        list1[index] = 0    # Replace -ve nos by zero
    replaceByZero(list1, index + 1)

replaceByZero(list0, 0)
print(list0)  # here list0 & list1 points to same list

# o/p : [10, 0, 50, 0]