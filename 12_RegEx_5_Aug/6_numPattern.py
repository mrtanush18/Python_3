import re

num = 123-456-7890

pattern = '(\d\d\d-\d\d\d-\d\d\d\d)' # \d{}

sample = input('Plz enter a number: ')

match = re.search(pattern,sample)

if match:
    print(match.group())
else:
    print('Invalid string')

# o/p : 
# Plz enter a number: 000-000-0000
# 000-000-0000   

# Plz enter a number: 00
# Invalid string 