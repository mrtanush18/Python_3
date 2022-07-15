dict = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}

print(dict)

# modify value without changing key

for k,v in dict.items():
    new_v = k**2
    dict[k] = new_v

print(dict)

# o/p :
# {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}