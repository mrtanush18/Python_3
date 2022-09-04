import re

str1 = "i like python programming"

pattern = '[i-p]'

match = re.findall(pattern, str1)

# print(match)

if len(match) > 0:
    print(match)       
else:
    print('no match')


# o/p: ['i', 'l', 'i', 'k', 'p', 'o', 'n', 'p', 'o', 'm', 'm', 'i', 'n']
