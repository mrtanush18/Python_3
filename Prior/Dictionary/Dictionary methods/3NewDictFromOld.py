# 1) Create a dict with the list of keys [‘one’,’One’,’ONE’] and give them each the value of 1.
my_dict= dict.fromkeys(['one','two','three'],1)
print(my_dict)


# 2) Shallow copy using d.copy() method
d = {1:'one',2:'two',3:'three',4:{'name':'tanush','contact':982}}
d_cpy = d.copy()

print(d) # {1: 'one', 2: 'two', 3: 'three', 4: {'name': 'tanush', 'contact': 982}}
print('copy of d: ',d_cpy) # copy of d:  {1: 'one', 2: 'two', 3: 'three', 4: {'name': 'tanush', 'contact': 982}}

d[1] = 'notOne' 
d[4]['contact'] = 999

print(d) # No CHANGE ONE level deep
# {1: 'notOne', 2: 'two', 3: 'three', 4: {'name': 'tanush', 'contact': 999}}

print('Any changes in cpy of d? ',d_cpy) # IT CHANGES in two level deep
# Any changes in cpy of d?  {1: 'one', 2: 'two', 3: 'three', 4: {'name': 'tanush', 'contact': 999}}
