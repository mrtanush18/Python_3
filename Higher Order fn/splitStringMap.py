# Split strings in list & store in list

list1 = ['sat',"bat","cat"]

result = map(list, list1)  # passed inbuilt list fn

print(list(result))        # typecast

# o/p : [['s', 'a', 't'], ['b', 'a', 't'], ['c', 'a', 't']]