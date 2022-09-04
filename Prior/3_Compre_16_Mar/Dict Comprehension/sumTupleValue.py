# desired o/p : {(0,1):1, (1,0):1, (0,0):0, (1,1):2}

dict = {(i,j) for i in range(2) for j in range(2)} 
print(dict)

# for i in range(2):
#     for j in range(2):
#         dict.fromkeys((i,j),'')

# print(dict)