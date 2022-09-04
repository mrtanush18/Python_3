# Python program to validate an Email

# import re module

import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,3}\b' # .co or.com

def check(email):

	if(re.fullmatch(regex, email)):
		print("Valid Email")

	else:
		print("Invalid Email")

email = "svk23@gmail.co.uk"
check(email)

email = "my.ownsite@our-earth.org"
check(email)

email = "ankitrai326.com"
check(email)
    
email = "janed@us.gov"
check(email)

email = "registrar-www@mit.edu"
check(email)

email = "no-reply@t.mail.coursera.org"
check(email)

email = "mail@eduinrus.ru"
check(email)

# o/p:
# Valid Email
# Valid Email    
# Invalid Email  
# Valid Email    
# Valid Email    
# Valid Email    
# Valid Email    



















# import re

# str1 = 'sureshvjadhav@gmail.com'

# pattern1 = '(.)@(.)(.)(\.com)'

# result1 = re.findall(pattern1,str1)
# print(result1)

# # result2 = re.findall(pattern2,str1)
# # # print(result2)

# if (len(result1) > 0) :
#     print("yes, correct mail format")
# else:
#     print('no')