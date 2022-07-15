dict = {0:'a',1:'b',2:'c',3:'d',4:'e',5:'f'}

toExtract = {i : dict[i] for i in [0,1,2]}

print(toExtract)

# WRONG :
# toExtract = {k2:v2 for k2 , v2 in dict.items() if k2 == 0 or 1 or 2}
# print(toExtract)

# LONG WAY : 
# dict = {0:'a',1:'b',2:'c',3:'d',4:'e',5:'f'}
# toExtract = {}
# size = int(input('No. of keys?'))
# keys = []
# print("Enter key to extract into new dictionary")

# for i in range(size):
#     items = int(input())
#     keys.append(items)

# toExtract = {keys[i]:v2 for i in range(len(keys)) for k2 , v2 in dict.items() if k2 == keys[i]}

# print(toExtract)