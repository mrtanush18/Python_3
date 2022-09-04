import re

ip1 = "0.0.0.0"
ip2 = '12.234.245.234'
ip3 = '123.234.123.42'
ip4 = '913.5.6.7'
ip5 = '1'
ip6 = '12'
ip7 = '123'
ip8 = '256'
ip9 = '251.234.3.5' 
ip10 = "255.255.255.255"

pattern = '([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'
#  single digits 0 to 9 or 2 digits or 3 digits starting from 1 or 3 digits starting from 2 or 3 digits starting from 25 (repeat this pattern 4 times as ipv4)
match = bool(re.match(pattern, ip10))

print(match)


# o/p : True