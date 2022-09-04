# string contains vowels or not?

string1 = "it is not easy to be you"

set2 = {'a','i','e','o','u'}
flag = 0

set1 = set(string1)

print(set1)

for item in set1:
    if item in set2:
        flag = flag + 1

if flag == 5:
    print('true',flag)
else:
    print('false',flag)


# o/p : {'b', 'a', 'n', 'y', ' ', 'o', 'u', 's', 't', 'i', 'e'}
# true 5