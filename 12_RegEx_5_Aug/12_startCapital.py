import re

str1 = "My Word"

pattern = '[A-Z]'

result = re.findall(pattern, str1)

# print(result)

if result:
    print(len(result), 'match')
else:
    print('No match')

# o/p: 2 match