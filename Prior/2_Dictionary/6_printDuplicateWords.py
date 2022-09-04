# Count number of duplicate words in sentence and print them

string = input('Enter sentence: ')

# count = 1

# for i in string:
#     if i == ' ':
#         count = count + 1

for i in range(1):
    words = string.split()   # split returns a list so no need to append in new list
print(words)

words2 = {}

for j in words:
    if j in words2:
        words2[j] = words2[j] + 1
    else:
        words2[j] = 1

print(words2)

print("Duplicate words: ", end='')
for key, value in words2.items():
    if(words2[key] > 1):
        print(key ,":",value, end = ' ')


# o/p :
# Enter sentence: a fox jumps over a fox
# ['a', 'fox', 'jumps', 'over', 'a', 'fox']
# {'a': 2, 'fox': 2, 'jumps': 1, 'over': 1}
# Duplicate words: a : 2 fox : 2