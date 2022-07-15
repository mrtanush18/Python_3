dict = {'a': 100 , 'b': 200 , 'c': 400}

sum = 0

for item in dict:
    sum = sum + dict[item]

print(sum) 

# o/p : 700

# >> CONCAT THE KEYS INTO SINGLE STRING

key = ""

for k in dict:
    key = key + str(k)  # concat string 

print(key)  

# o/p : abc
