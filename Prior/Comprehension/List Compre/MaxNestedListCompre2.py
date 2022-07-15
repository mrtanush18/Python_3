# Find max element from sub lists without using max method in list comprehension (had to use functions)

nested_list = [[1,2,3],[4,5,6],[7,8,9]]

sub_list_max = []

def getMaxSubElement(sub_list):
   max = 0
   for j in sub_list:    # used only 1 loop as already we have inner lists in sub_list
        if max < j:
            max = j
   sub_list_max.append(max)
    

list_compre = [getMaxSubElement(sub_list) for sub_list in nested_list]

print(sub_list_max)

# o/p : [3, 6, 9]