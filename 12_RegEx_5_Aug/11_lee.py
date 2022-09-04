import re

str1 = "shane mnleeee bowls to break lee"
str2 = "shane le bowls to break le"

pattern = r'\blee\b'

result = re.findall(pattern, str1)

# print(result)

if len(result) > 0:
    for i in result:
        print(i, end=" ")
if len(result) == 0:
    print('No match')

