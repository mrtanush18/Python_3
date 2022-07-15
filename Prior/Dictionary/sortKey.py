dict = {}

dict[2] = 56
dict[1] = 2
dict[5] = 12
dict[4] = 24
dict[6] = 18
dict[3] = 323

print(dict)

num = 1
new_dict = {}

while(num <= len(dict)):
    for key,value in dict.items():
        if key not in new_dict and key == num:
            new_dict[key] = value
            num = num + 1

print(new_dict)

# o/p:
# {2: 56, 1: 2, 5: 12, 4: 24, 6: 18, 3: 323}
# {1: 2, 2: 56, 3: 323, 4: 24, 5: 12, 6: 18}