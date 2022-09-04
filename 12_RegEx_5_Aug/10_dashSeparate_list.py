import re

strings = ['99921-58-10-7', '9971-5-0-10-0', '960-425-059-0', '80-902734-1-6', '910975229-0-x']

regex = r'\b[0-9-]+[A-Za-z0-9]+\b'

# input1 = input('Enter a string: ')

for i in strings:
	result = re.fullmatch(regex, i)

# print(result)

	if(result):
		print('valid string')
	else:
		print('Invalid string')

# o/p:
# valid string
# valid string   
# valid string   
# valid string   
# valid string   
