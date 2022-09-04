list = [1, 2, 3, 2, 5, 2, 6]

# size = int(input("Enter size of list: "))
# print("Enter items in list: ")
# HOW TO TAKE INPUT IN LIST
# for i in range(size):
#     element = int(input())
#     list.append(element)

print(list)

toFind = int(input("What to find? "))

# HOW TO LOCATE & PRINT INDEX of list item (for j in list: won't print index only value)

for i in range(len(list)):  # i = 0,1,2...
    pos = 1
    if list[i] == toFind:  
        pos = pos + i
        print(toFind, "at position", pos)

# We have to use list[i] not i to access elements ---> for i in range(len(list)): 
# pos = 1 inside loop to reset it to one, each time 2 is found

# o/p:
# [1, 2, 3, 2, 5, 2, 6]
# What to find? 2
# 2 at position 2
# 2 at position 4
# 2 at position 6




