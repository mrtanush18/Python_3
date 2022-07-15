list1 = [1,2,3,4,5,6,7,8,9]

# o/p : [[1,2,3,4],[5,6,7,8],[9]]

print("Enter range till which list elements should be grouped")

r = int(input())

nested_list = [list1[i:i+r] for i in range(0, len(list1), r)]

print(nested_list)