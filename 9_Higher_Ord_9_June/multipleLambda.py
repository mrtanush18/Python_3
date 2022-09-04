# Keep revising

ans = [lambda x=x:x*5 for x in range(1,12)]
list0= []

for j in ans:
    list0.append(j())   #j calls function
    # print(j(), end=",")   #OR

print(list0)

# o/p : [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55]