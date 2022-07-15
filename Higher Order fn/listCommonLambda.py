# Print common elements in both lists, o/p : 3,5

list1 = [1,3,4,5,7]
list2 = [2,3,5,6]

ans = lambda x,y:set(x).intersection(set(y))

print(ans(list1,list2))

# print(type(ans))

# print(set(list1).intersection(set(list2)))

# o/p : {3, 5}