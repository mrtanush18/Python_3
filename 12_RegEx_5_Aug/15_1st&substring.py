import re
from statistics import mode

str1 = 'python is a language and python is best'

substring = input('Enter substring to check in string: ')

pattern = '[a-z]+|[A-Z]+'

match = re.findall(pattern, str1)

print(match)

flag = 0

for i in match:
    if i == substring and i == mode(match):
        flag = 1
        break
    else:
        print(substring, ' is not 1st element')
        break

if flag == 1:
    print (substring, ' is a 1st element & a substring')


# o/p: Enter substring to check in string: python
# python  is a 1st element & a substring