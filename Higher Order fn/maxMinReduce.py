import functools

list0 = [10,20,40,50,-60]

# max1 = functools.reduce(max, list0)
# min1 = functools.reduce(min, list0)

# 2nd Method :

def findMax(x,y):
    print(x, y)
    return x if x > y else y

def findMin(x,y):
    print(x, y)
    return x if x < y else y

max1 = functools.reduce(findMax, list0)

min1 = functools.reduce(findMin, list0)

print("Maximum is: ",max1, ", Minimum is:", min1)


'''
o/p:
10 20
20 40
40 50
50 -60
10 20
10 40
10 50
10 -60
Maximum is:  50 , Minimum is: -60
'''