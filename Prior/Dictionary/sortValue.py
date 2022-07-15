dict = {}

dict[2] = 56
dict[1] = 2
dict[5] = 12
dict[4] = 24
dict[6] = 18
dict[3] = 323

print(dict)

list = []

for value in dict.values():
    list.append(value)

print(list)

temp = 0

for i in range(0,len(list)):    
    for j in range((i+1),len(list)):  
        if(list[i] > list[j]):  
            temp = list[i]
            list[i] = list[j]
            list[j] = temp
        
print(list)

# o/p:
# {2: 56, 1: 2, 5: 12, 4: 24, 6: 18, 3: 323}
# [56, 2, 12, 24, 18, 323]
# [2, 12, 18, 24, 56, 323]