# Desired o/p  thru dict comprehension:
# {5:'f'}

dict = {0:'a',1:'b',2:'c',3:'d',4:'e',5:'f'}

# for i in range(5):
#     del dict[i]
# print(dict)

list = [0,1,2,3,4]

new = {k : dict[k] for k in dict.keys() - list}

print(new)

# o/p:
# {5:'f'}