# Find n max and min elements in tuple and return them as a new tuple

ogTuple = (3,7,1,18,9,10,12)
new = list(ogTuple)
print(new)
new.sort()   
print("Sorted list: ", new)  # [1, 3, 7, 9, 10, 12, 18]

size = int(input('Enter no. of max and min items to find: ')) # 3

minList = []
for j in range(0,size):    # as list is sorted just print first 'n' elements
    minList.append(new[j])
minTuple = tuple(minList)

print('Min elements: ', minTuple)  

maxList = []
maxList = new[-size:]
maxTuple = tuple(maxList)
print('Max elements: ',maxTuple)

finalTuple = minTuple + maxTuple

print(finalTuple)