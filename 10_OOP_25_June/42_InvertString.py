# Inverted string using list slicing  [ : : ] method
# Other way : slice(start, stop, step)
# https://www.geeksforgeeks.org/string-slicing-in-python/

str1 = "practise.py"
new = ""
index = 0

for i in range(len(str1)):
    if str1[i] == ".":
        index = i
print(index)
print(len(str1))

print(str1[index:len(str1)])
print(str1[0:index])        #  rhs of : is excluded so till element 8(index) is printed
print(str1[index:len(str1)] + str1[0:index])


# o/p : 
# 8
# 11
# .py
# practise        
# .pypractise