# Except 15 replace other words with space
import re

str1 = '15th August is celebrated as independence day'

pattern = '[a-z|A-Z]'

replace = ' '

new_str1 = re.subn(pattern, replace, str1)

print(new_str1)


# o/p:
# ('15
#            ', 37)