# REVERSE LIST by appending last element to NEW LIST & keep decrementing length by 1
# TC = O(n)

ogList = [100,-56,5,6,7,8]
reversed_list = []

print('OG list: ',ogList)

length = len(ogList)

count = 0

for i in range(length-1, -1, -1): # decrementing loop,(start=5, end at 0, decrement by -1)
    temp = ogList[i]    # 8 @ index 5, and so on
    reversed_list.append(temp)
    count = count + 1       # No. of iterations

print('Reversed list: ',reversed_list)
print('No. of iterations:',count)

# o/p:
# OG list: [100, -56, 5, 6, 7, 8]
# Reversed list:  [8, 7, 6, 5, -56, 100]
# No. of iterations: 6