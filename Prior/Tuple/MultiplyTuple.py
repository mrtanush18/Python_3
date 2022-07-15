# o/p : (5,35,56,80)

tuple = (1,5,7,8,10)

for i in range(0,len(tuple)-1):   # 0 1 2  *  1 2 3
    print((tuple[i]*tuple[i+1]))











# wrong :
# for i in range(1,len(tuple),2): # 5 , 8
#     for j in range(0,(i+3),2): # 1 , 7 , 10
#         product = tuple[i]*tuple[j]
#         print(product)