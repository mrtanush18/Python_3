import re

aadhar = '2310 4560 6789'

pattern = '^[2-9]{1}[0-9]{3}\\s[0-9]{4}\\s[0-9]{4}$'

match = re.search(pattern, aadhar)

# print(match)

if(re.search(pattern, aadhar)):
	print("Valid")

else:
	print("Invalid")


# o/p: Valid