# Take user input for a 3 level nested dictionary and print emp1 and 2 details

dict = {}

for i in range(2):
    outer_key = input('\nEnter outer key: ')  
    value = {}

    for j in range(1):  
        key1 = input('\nEnter inner key: ')  
        value1 = {}
        value[key1] = value1              

        dict[outer_key] = value         # IMP (TO AVOID OVERWRITING OF VALUES)  

        for k in range(2):
            key2 = input('\nEnter innermost key: ')  
            value2 = input('Enter innermost value: ')

            value1[key2] = value2

print("\n3 level dictionary: ",dict)

# {key :   {key1 :   {innermost key2 : value2}}, key1 : {innermost key2 : value2}}}
# ^        ^         ^                      
# dict     value     value1

for key,value in dict.items():                
    print("\nEmp_id: ",key)

    for key1,value1 in value.items():
        print("key1: ",key1)

        for key2,value2 in value1.items():
            print(key2,":",value2)



'''
# o/p :
3 level dictionary:  {'E1': {'mob1': {'p1': '981', 'p2': '982'}}, 'E2': {'mob2': {'p3': '983', 'p4': '984'}}}

Emp_id:  E1
key1:  mob1
p1 : 981
p2 : 982

Emp_id:  E2
key1:  mob2
p3 : 983
p4 : 984
'''

# i/p : 
# Enter outer key: E1
# Enter inner key: mob1
# Enter innermost key: p1  
# Enter innermost value: 981
# Enter innermost key: p2
# Enter innermost value: 982

# Enter outer key: E2
# Enter inner key: mob2
# Enter innermost key: p3
# Enter innermost value: 983
# Enter innermost key: p4
# Enter innermost value: 984