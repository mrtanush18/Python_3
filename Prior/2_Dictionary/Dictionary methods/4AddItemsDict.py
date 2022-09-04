# 1) ADD ITEMS TO DICT
dict = {}
print(dict)
# {}

dict['Mon'] = 1
print(dict)
# {'Mon': 1}

# 2) ADD VALUES TO SAME KEY

myCars = {}

myCars.setdefault("Cars",[]).append("BMW")

print(myCars)
# {'Cars': ['BMW']}

myCars.setdefault('Cars',[]).append("Toyota")

print(myCars)
# {'Cars': ['BMW', 'Toyota']}

# 3) COPY ITEMS OF DICT 2 INTO DICT 1 WITHOUT LOOPING

dict1 = {1:'one',2:'two',3:'three'}
print(dict1)

dict2 = {4:'four',5:'five'}
print(dict2)

dict1.update(dict2)
print(dict1)

