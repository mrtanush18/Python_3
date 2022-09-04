import re

str1 = '12:15AM'

pattern = '(1[012]|[1-9]1[012]):([0-5][0-9])(am|pm|AM|PM)'

match = re.match(pattern,str1)

print(match)


# mac address, pincode, DL, html, tags, ipv6, mastercard, substitute method