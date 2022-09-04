list = [(4,2),(3,4),(3,4),(3,4),(3,4)]
# o/p : [(4,2,1),(3,4,4)] # count

new = {}
count = 0
new_list = []

# count tuples
for i in range(len(list)):
    if list[i] not in new:
        new[list[i]] = 1
        continue
    if list[i] in new:
        new[list[i]] = new[list[i]] + 1

# print(new)

# append count to tuple
for k,v in new.items():
    new_tuple = k+(v,)
    new_list.append(new_tuple)

print(new_list)



