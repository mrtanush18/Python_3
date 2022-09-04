# HW : Print dictionary items in foll. format :

# emp_id : emp1
# name : sam
# job : developer

# emp_id : emp2
# name : jon
# job : swe

dict = {}

size = int(input('\nEnter no. of keys in dict: '))

for i in range(size):
    value = {}

    main_key = input('\nEnter outer key: ')

    key1 = input('\nEnter key1: ')
    value1 = input('Enter value1: ')
    value[key1] = value1

    key2 = input('\nEnter key2: ')
    value2 = input('Enter value2: ')
    value[key2] = value2

    dict[main_key] = value

print("\n",dict)

for key,value in dict.items():
    print("\nEmp_id : ",key)
    
    for key,value in value.items():
        print(key,":",value)

# o/p :
# {'emp1': {'name': 'tanush', 'age': '22'}, 'emp2': {'name': 'rach', 'age': '20'}}     

# Emp_id :  emp1
# name : tanush
# age : 22

# Emp_id :  emp2
# name : rach
# age : 20


# _______________________________________________________________________________________
# >> To print nested value when you know outer key

# dict = {}

# size = int(input("Enter main size"))

# for i in range(1,(size+1)):

#     dict[i] = {}
    
#     company = input('Enter company'+ str(i) + "")
#     os = input('Enter os'+ str(i) + "")
#     price = input('Enter price'+ str(i) + "")

#     dict[i]['company'] = company
#     dict[i]['os'] = os
#     dict[i]['price'] = price
 

# print(dict)
# print(dict[1]['company'])
# print(dict[2]['company'])
# print(dict[1]['price'])
# print(dict[2]['price'])



