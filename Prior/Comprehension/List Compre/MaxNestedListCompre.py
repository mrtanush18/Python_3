# Find max element from sub lists 
# Found using max method in list comprehension

list = [[1,2,3],[4,5,6],[7,8,9]]
max_element = [max(i) for i in list]
print(max_element)

# o/p:
# [3, 6, 9]