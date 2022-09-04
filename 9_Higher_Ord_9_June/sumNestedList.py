import functools

list0 = [[1,2,3],[4,5,6],[7,8,9]]

flat_list = sum(list0, [])
print(flat_list)

def sumList(x,y):
    print(x,y)
    return x+y

ans = functools.reduce(lambda x,y:x+y, flat_list)
print(ans)

# initializer=400
# ans = functools.reduce(sumList, flat_list, initializer)
# print(ans)

'''
Error: TypeError: 'int' object is not iterable (single no. can't be converted to list)
ans = map(sum, flat_list)
print(list(ans))
'''