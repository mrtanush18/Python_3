list = [1,2,3,4]

def myFunc(x):
    x[0] = 20

myFunc(list)
print(list)

# o/p : [20, 2, 3, 4]

#2
# list = [1,2,3,4]

# def myFunc(x):
#     x = [20,30,40]

# myFunc(list)
# print(list)

# o/p : [1, 2, 3, 4]

#3
# list = [1,2,3,4]

# def myFunc(x):
#     x = 10

# myFunc(list)
# print(list)

# o/p : [1, 2, 3, 4]

#4
# def swap(x,y):
#     temp = x
#     x = y
#     y = temp
#     return x,y

# a,b = swap(10,20)
# print(a,b)

# o/p: 20 10