# Dynamic Nested dictionary : {emp1:{name: , job:}}

dict = {}
size = int(input("No. of outer keys? "))

for i in range(size):
    outer_key = input('\nOuter key ')

    value = {}  # Create new dict

    for j in range(2):  # Input values in new dict
        key, val = input('\nEnter key & value: ').split()
    
        value[key] = val
        dict[outer_key] = value

print(dict)
# o/p :
# {'emp1': {'name': 'tanush', 'mob': '981'}, 'emp2': {'name': 'rachit', 'mob': '982'}}

'''
# WORKING
for i in range(2):

i = 0 : outer_key = input('\nOuter key ') , value = {}  

for j in range(2): 
j = 0
input('\nEnter key & value: ') , value[key] = val , dict[outer_key] = value

j = 1
input('\nEnter key & value: ') , value[key] = val , dict[outer_key] = value

i = 1 : REPEAT ABOVE PROCESS
'''