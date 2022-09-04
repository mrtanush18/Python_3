import re

pan = 'TUVYW1234A'

pattern = '^[A-Z]{5}[0-9]{4}[A-Z]{1}$'

match = re.search(pattern, pan)

# print(match)

if(re.search(pattern, pan)):
	print("Valid")

else:
	print("Invalid")

# o/p: Valid