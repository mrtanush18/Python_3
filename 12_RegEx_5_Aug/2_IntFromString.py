# Extract int from string

import re

str1 = "there is a phone number 12345678 and his age : 23"

pattern = '(\d+)'

match = re.search(pattern, str1)

print(match)

if match:
  print(match.group())  # returns the part of the string where there is a match.
else:
  print("pattern not found")

# o/p : 
# <re.Match object; span=(24, 32), match='12345678'>
# 12345678