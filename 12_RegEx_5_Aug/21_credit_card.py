import re

str1 = '4110241022223' # 13 or 16 digits

pattern = '^[4]{1}[0-9]{12,15}$'

match = re.search(pattern, str1)

# print(match)

if(match):
    print('Valid')
else:
    print('Invalid')

# o/p: Valid