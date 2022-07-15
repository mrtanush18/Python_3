dict = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}

dict_cpy = dict.copy()
print(dict_cpy)

# dict_cpy[1] = 'ONE'
# dict_cpy[2] = 'TWO'

dict_cpy.update({1 : 'ONE', 2: 'TWO'})
print(dict_cpy)