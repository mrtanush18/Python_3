dict = {1:'one', 2:'two', 3:'three'}
dict2 = {4:'four', 5:'five', 6:'six'}

dict.update(dict2) # merged dict
print(dict)

Lkeys = []
Lvalues = []

for keys,values in dict.items():   # append keys and values into separate lists
        Lkeys.append(keys)
        Lvalues.append(values)

print(Lkeys)
print(Lvalues)

new = {}

i = -1

while(i!= - len(Lkeys)-1):      # reverse order of keys 
    new.update({Lkeys[i] : Lvalues[i]})
    i = i - 1

print(new)

# o/p
# {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six'}
# [1, 2, 3, 4, 5, 6]
# ['one', 'two', 'three', 'four', 'five', 'six']
# {6: 'six', 5: 'five', 4: 'four', 3: 'three', 2: 'two', 1: 'one'}

'''
# Dry run : 

i = -1

=> while i != -7  => (-6-1)
      new.update(Lkeys[-1] : Lvalues[-1]
      i = -1 -1 => -2
      
'''
