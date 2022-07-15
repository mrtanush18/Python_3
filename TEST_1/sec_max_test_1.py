# 2nd largest no. from user defined list

list1 = []

size = int(input("Enter no. of elements: "))

print("Enter elements: ")

for i in range(size):
    num = int(input())
    list1.append(num)

sorted = list1.sort()
print(list1)

max1 = max(list1)
sec_max = list1[0]

print(max1)

for i in list1:
    if i > sec_max and i != max1:
        sec_max = i

print(sec_max)

