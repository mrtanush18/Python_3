import re

str1 = 'http://www.google.com'
str2 = 'https://www.google.com'
str3 = 'https://www.google.net/amp/5'
str4 = 'www.google.com'

pattern = r'\bhttp|https+://www+\.[A-Za-z0-9._%+-]+[A-Z|a-z]{2,3}/+[/A-Za-z0-9]+\b'

if(re.fullmatch(pattern, str4)):
	print("Valid URL")

else:
	print("Invalid URL")

# o/p: Invalid URL