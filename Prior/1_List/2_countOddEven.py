list = []
size = int(input("Size: "))

# Populate list
print("Enter odd and even elements")
for i in range(size): 
    element = int(input())
    list.append(element)

# set count to zero
even_count = 0 
odd_count = 0 

# main logic
for i in list:
    if i%2 == 0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1

print(list)

print("even numbers: ", even_count, "& odd numbers: ", odd_count)

# o/p
# [1, 2, 3, 4, 5, 6]
# even numbers:  3 odd numbers:  3