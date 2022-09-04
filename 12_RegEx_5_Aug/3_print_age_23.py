# Extract "age : 23" from string
import re

str1 = "there is a phone number 12345678 and his age : 23"

pattern = '\d+' # 1 or more digits

pattern2 = '\s+'

match = re.findall(pattern, str1)

match2 = re.split(pattern2,str1)

print(match)
print(match2)

for i in range(len(match2)):
  if match2[i] == ':':
    print(match2[i-1], match2[i], match2[i+1])

# o/p :
# ['12345678', '23']
# ['there', 'is', 'a', 'phone', 'number', '12345678', 'and', 'his', 'age', ':', '23'] 
# age : 23