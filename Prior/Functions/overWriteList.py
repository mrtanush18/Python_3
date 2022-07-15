# Overwrite values of list

list = [1,2,3,4]

def overWriteList(NewList):
    value = NewList[0]*5
    for i in range(len(NewList)):
        NewList[i] = value
        value = value + 1
    return NewList

x = overWriteList(list) # called fn & passed entire list !!
print(x)



