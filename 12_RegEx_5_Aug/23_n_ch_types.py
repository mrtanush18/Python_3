import re

str1 = 'I prefer Python 3, not C++'

pattern = '[A-Z]'
pattern2 = '[a-z]'
pattern3 = '\d+'
pattern4 = '[_!_+_*_$]'

match = re.findall(pattern, str1)
match2 = re.findall(pattern2, str1)
match3 = re.findall(pattern3, str1)
match4 = re.findall(pattern4, str1)

print('There are ',len(match), 'uppercase, ', len(match2),'lowercase, ', len(match3),'numbers, ',len(match4), 'special characters')

# o/p: There are  3 uppercase,  14 lowercase,  1 numbers,  2 special characters