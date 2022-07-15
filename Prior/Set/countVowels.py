# count no of vowels in string using sets

string1 = "it is not easy to be you"

set2 = {'a','i','e','o','u'}
count = 0

# set1 = set(string1)

# print(set1)

for item in string1:
    if item in set2:
        count = count + 1 

print(count)  # 9