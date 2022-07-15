# Swap 1st & last items in list

num = int(input("size of list: "))

list = []

for i in range(num):
    element = int(input())
    list.append(element)

list[0],list[-1] = list[-1],list[0] # comma assignment

print(list)

'''
o/p :
size of list5
1
2
3
4
5
[5, 2, 3, 4, 1]
'''


'''
Swap without using method: (find length of list and swap)

# length = len(list) 
# temp1 = list[0]
# temp2 = list[length-1]

# list[length-1] = temp1
# list[0] = temp2

print(list)
'''

'''
Swap using pop
     
first = list.pop(0)  
last = list.pop(-1)
     
list.insert(0, last) 
list.append(first)  
'''