keys = [1,2,3]

values = ['one','two','three']

# dict = {}

# for i in keys:
#     for j in values:
#         dict[i] = j

# print(dict)

dict = {keys:values for keys,values in zip(keys,values)}

print(dict)

# o/p : {1: 'one', 2: 'two', 3: 'three'}