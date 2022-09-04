list = []

size = int(input("Enter no. of elements in list: "))

print("Enter elements: ")
for i in range(size):
    element = int(input())
    list.append(element)

print(list)

max_element = list[0]
sec_max_element = list[0]

for element in list:
    if(max_element < element):
        max_element = element

print("Max element is",max_element)

for element in list:
    if(sec_max_element < element and element != max_element):
        sec_max_element = element

print("2nd max element is",sec_max_element)

# o/p:
# max element is 60
# 2nd max element is 50