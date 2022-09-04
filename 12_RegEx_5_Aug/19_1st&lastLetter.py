import re

str1 = 'k'
str2 = str1.upper()
print(str2)

pattern = '[A-Za-z0-9]'

match = re.findall(pattern,str2)

# print(list(match))

if(list(match)[0] == list(match)[-1]):
	print('Valid')
else:
	print('Invalid')

# o/p:
# K
# Valid

