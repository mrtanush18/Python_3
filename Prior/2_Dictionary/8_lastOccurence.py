# Take input from user elements of list and element to find last & 2nd last occurence

list = []
size = int(input('Enter no. of elements in list'))
print('Enter elements of list')

for i in range(size):
    element = int(input())
    list.append(element)

print(list)
# o/p:
# [5, 4, 3, 4, 7, 2, 4]

length = len(list)
toFind = int(input('Enter number to find last occurence of'))

for i in range(0,length,1):
    if list[i] == toFind:
        pos1 = i
        print("2nd last occurence of",toFind, "is at position", pos1+1)
        break

# o/p 
# 2nd last occurence of 4 is at position 2

for i in range(0,length,1):
    if list[i] == toFind:
        pos = i

print("Last occurence of",toFind, "is at position", pos+1)

# o/p
# Last occurence of 4 is at position 7


# for i in range((length-1),0,-1): 
# # start, 'stop', step(interval) to traverse list from end