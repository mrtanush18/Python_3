import re

str1 = input('Enter string: ')

pattern = '[^A-Za-z0-9]'

match = re.findall(pattern, str1)

if(match):
    print('Invalid input, there are', len(match), 'invalid characters')
else:
    print(match)

# o/p:
# Enter string: a_$B{}cd
# Invalid input, there are 4 invalid characters