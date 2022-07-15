#1) Max element in list
list = [[1,2,3],[4,5,6],[7,8,9]]
max = 0
max_list = []

for i in range(len(list)):
    for j in list[i]:
        if max < j:
            max = j
    max_list.append(max)

print(max_list)

# o/p:
# [3, 6, 9]