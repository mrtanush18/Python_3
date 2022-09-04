# Using pow method 

list2 = [1,2,3]
cubeList2 = []
for values in list2:
    cubeList2.append(pow(values,3))
    
print(cubeList2,"pow method used")

# o/p: [1, 8, 27] pow method used

# Without using pow
# list = [1,2,3]
# cubeList = []

# for value in list:
#     cubeList.append(value*value*value)

# print(cubeList,"pow method not used")

# o/p: No pow [1, 8, 27]