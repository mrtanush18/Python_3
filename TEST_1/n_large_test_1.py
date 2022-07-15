# n no. of largest no.

list1 = []

size = int(input("Enter no. of elements: "))

print("Enter elements: ")

for i in range(size):
    num = int(input())
    list1.append(num)

# sorted = list1.sort()
print(list1)


n = int(input("Enter no. of large items you want from list: "))
n_max = []

if n > len(list1):
    print("Invalid")
else:
    for i in range(0,n):
        max1 = 0
        for j in range(len(list1)):
            if max1 < list1[j]:
                max1 = list1[j]
        list1.remove(max1)
        n_max.append(max1)

print(n_max)

