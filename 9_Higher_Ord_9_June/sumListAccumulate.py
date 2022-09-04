import itertools

list0 = [[1,2,3],[4,5,6],[7,8,9]]

flat_list = sum(list0, [])
print(flat_list)

ans = itertools.accumulate(flat_list, lambda x,y:x+y)

print(list(ans))