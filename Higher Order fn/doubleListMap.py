list0 = [1,2,3,4]

# 1) NORMAL WAY to double list items :

def double(list1):
    doubled_list = [item*2 for item in list1]
    print(doubled_list)

double(list0)

# 2) Using MAP

def fn(a):                         # maps 'a' to each list item
    return a + a

result = map(fn,list0)

print("Using Map: ",list(result))  # typecast 

# 3) Using LAMBDA fn (nameless fn), short form of map

ans = map(lambda a:a+a, list0)      # can only have one expression like in compre
print("Using Lambda: ",list(ans))

'''
o/p :
[2, 4, 6, 8]
Using Map:  [2, 4, 6, 8]
Using Lambda:  [2, 4, 6, 8]
'''

