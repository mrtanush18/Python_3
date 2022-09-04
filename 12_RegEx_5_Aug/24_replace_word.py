import re

str1 = 'Ít is raining outside' # sunny
str2 = 'Thank you very very much' # so so

pattern1 = 'raining'
pattern2 = 'very'

replace1 = 'sunny'
replace2 = 'so'

new_str1 = re.subn(pattern1, replace1, str1)
new_str2 = re.subn(pattern2, replace2, str2)

print(new_str1[0])
print(new_str2[0])

# o/p:
# Ít is sunny outside
# Thank you so so much