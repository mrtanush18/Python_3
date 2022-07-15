# Swap second last with first item

list = []
list_size = int(input("Enter size of list"))

print("Enter items in list")

for i in range(list_size):
    item = int(input())
    list.append(item)

print(list)

list[0], list[list_size-2] = list[list_size-2], list[0]

print(list)

'''
o/p:

Enter size of list5
Enter items in list
1
2
3
4
5
[1, 2, 3, 4, 5]
[4, 2, 3, 1, 5]
'''

# 0 is first , -1 is last
# From back     , -10 , ...................................... -1
# Front             0 , ......................................  9
# Ex.               1    2    3    4    5    6    7    8    9   10

