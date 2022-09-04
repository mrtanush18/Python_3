dict = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}

# print(dict)

dict_cpy = dict.copy() # copy to work with

# print(dict_cpy)

# 1) pop
pop_one = dict_cpy.pop(1)

# print(dict_cpy)
# print(pop_one)

# o/p:
# {2: 'two', 3: 'three', 4: 'four', 5: 'five'}
# one

# 2) popitem() : no args, removes items in LIFO manner

popped_Item = dict_cpy.popitem()

# print(popped_Item,type(popped_Item)) 
# print(dict_cpy) 

# o/p:
# (5, 'five') <class 'tuple'>
# {2: 'two', 3: 'three', 4: 'four'}

# 3) clear()

dict_cpy.clear()
# print(dict_cpy) 

# o/p:
#  {}

# 4) del

dict_cpy2 = dict.copy() # copy to work with
print(dict_cpy2)
# o/p: {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}

del dict_cpy2[1]
print(dict_cpy2)

del dict_cpy2
print(dict_cpy2)
# o/p : NameError: name 'dict_cpy2' is not defined.