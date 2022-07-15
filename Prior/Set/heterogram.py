# heterogram or not, every alphabet in word one time

string1 = "python" 
# set1 = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}

# flag = 0

# for i in range(len(string1)):
#     if string1[i] in set1:
#         flag = flag + 1
#     else:
#         flag = flag - 1

# if flag == len(string1):
#     print('heterogram',flag)
# else:
#      print('not a heterogram', flag)

# METHOD 2 :

lenString = len(string1)

copy = set(string1)

copy.discard(" ")

print(copy)

lenSet = len(copy)

if lenString == lenSet:
    print('true')
else:
    print('false')

# o/p : {'y', 'o', 'h', 't', 'n', 'p'}
# true