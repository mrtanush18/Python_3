#  Find number of unique elements 

list = [1,2,2,4,6,4,9,1]  
copy = []                          

for i in list:
    if i not in copy:        # second list to compare items with first one
        copy.append(i)

print("There are",len(copy),"unique elements in given list")
print("Unique elements: ",copy)

# o/p: There are 5 unique elements in given list
# Unique elements:  [1, 2, 4, 6, 9]


