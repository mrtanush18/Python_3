import re

str1 = 'I like Python'

str2 = str1[0:10]

# print(str2)

pattern = '[a-z]'

replace = '0'

# new = re.subn(pattern, replace, str2)
# print(new[0]+str1[10:len(str1)])

# Simple way: 
new = re.sub(pattern, replace, str1, count=8, flags=re.I)
print(new)

# o/p:
# 0 0000 000hon