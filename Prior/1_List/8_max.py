size = int(input("\nEnter no. of elements in list: "))
list = []

# populate list
for i in range(size):
    element = int(input())
    list.append(element)
print(list)

# Initialized max element
max_element = list[0]       # moved statement outside to reduce time complexity

# if any element is more than max assign it as max
for element in list:
    if(max_element<element): 
        max_element = element   
    
print('\nMax element is: ',max_element)

# o/p: [-100, -90, -80, -10, -70, -60, -50]
# Max element is:  -10
    


