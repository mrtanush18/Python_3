# Take user i/p to print key as list ex. a = [7,8,9]

test_dict = {'python': {"a" : 7, "b":9, "c":12}, 'is': {"a" : 8, "b":10, "c":13}, 'best': {"a" : 9, "b":11, "c":14}}

toPrint = input('Choose key from dict: ')

value = [v2 for k1, v1 in test_dict.items() for k2,v2 in v1.items() if k2 == toPrint]

print(value)

# O/P : 
# Choose key from dict: c
# [12, 13, 14]   



# NORMAL WAY : 
# value = []

# toPrint = input('Choose key from dict: ')

# for k1, v1 in test_dict.items():
#     for k2,v2 in v1.items():
#         if k2 == toPrint:
#             value.append(v2)

# print(value)















