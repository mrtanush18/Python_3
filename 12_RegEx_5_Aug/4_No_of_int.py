# Print no. of integers in string 

import re

str1 = "there is a phone number 12345678 and his age : 23"

pattern = '\d+'

match = re.findall(pattern, str1)

print(len(match))

# o/p : 2 