dict = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}

# 1) .get method to access values

# print(dict.get(1)) # one
# print(dict.get(6)) # None

# 2) .values() method 
# returns all values in the dictionary as a dictionary view object.
# This object can be converted into a set, tuple, list, or directly iterated through, based on the need.

dictValues = dict.values()
print(dictValues)

# 3) convert values to tuple
values_to_Tuple = tuple(dict.values())
print(values_to_Tuple)

# 4) convert values to list
values_to_List = list(dict.values())
print(values_to_List)

# o/p:
# dict_values(['one', 'two', 'three', 'four', 'five'])
# ('one', 'two', 'three', 'four', 'five')
# ['one', 'two', 'three', 'four', 'five']


