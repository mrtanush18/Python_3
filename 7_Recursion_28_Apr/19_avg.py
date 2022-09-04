list0 = [7,3,17,5,2] # avg = 6

def calcAvg(list1):
    if len(list1) == 0:
        return 0
    else:
        return list1[0] + calcAvg(list1[1:])

avg = calcAvg(list0)
print(avg//len(list0))

# o/p : 6