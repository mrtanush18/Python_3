import re, statistics
from statistics import mode

str1 = 'pythonv2thenafterv2v3ab44cd44yz44abc3z3z3z'

pattern = '\d+'

match = re.findall(pattern,str1)

print(mode(match))

# o/p: 3