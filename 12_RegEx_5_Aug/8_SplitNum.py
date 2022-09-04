import re

str1 = "i wake up in the morning at 8am on 10th of August,2022"

pattern = '\d+'

result = re.findall(pattern, str1)

new = []

if len(result) > 0:
    for i in result:
        if len(i) > 1:
            for j in range(len(i)):
                new.append(i[j])

result.extend(new)
# print(new)
print(result)


# o/p : ['8', '10', '2022', '1', '0', '2', '0', '2', '2']