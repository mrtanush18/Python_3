import re

str_list = ['axis bank', 'bank of america', 'the bank of india', 'infosys']

searchThis = input('What to search? ')

x = searchThis.split(' ')

print(x)

pattern = '[a-z|A-Z\s]*'  # axs bank

match2 = []
for i in str_list:
    match = re.findall(pattern, i)
    if len(match) > 0:
        match2.append(i)

print(match2)

list3 = []

for i in range(len(match2)):
    for j in range(len(x)):
        if x[j] == match2[i].split():
            print('123')
            list3.append(match2[i])

print(list3)


