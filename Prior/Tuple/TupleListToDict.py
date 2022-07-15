# Convert to dict
list = [('ram',23),('shyam',30),('dhaval',40)]
new_list = []
dict = {}

# convert list of tuples to list
for tuple in list:
    for value in tuple:
        new_list.append(value)

print(new_list)
# o/p : ['ram', 23, 'shyam', 30, 'dhaval', 40]

key = []
value = []

# As keys, values are alternate items in list
for i in range(len(new_list)):
    if i%2 == 0:
        key.append(new_list[i])
    if i%2 != 0:
        value.append(new_list[i])

print(key)
print(value)
# o/p :
# ['ram', 'shyam', 'dhaval']
# [23, 30, 40]

dict = {key:value for key,value in zip(key,value)}  # zip(k,v)

print(dict)

# o/p : {'ram': 23, 'shyam': 30, 'dhaval': 40}




# print(list[0][1])
# o/p : 23