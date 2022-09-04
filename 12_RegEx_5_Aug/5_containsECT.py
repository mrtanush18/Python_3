# Print ect from str1

import re

str1 = "python is a object oriented language"

pattern = '(.)ect'

result = re.findall(pattern, str1)
print(result)

if len(result) > 0:
    print("yes, contains ect")
else:
    print('no')

# o/p:
# ['j']
# yes, contains ect