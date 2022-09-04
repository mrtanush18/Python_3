# No class or Inheritance, Polymorphism, Composition needed as list has no attributes

list0 = [-25,-10,-7,-3,2,4,8,10]
# [-10,2,8] , [-7,-3,10]

all = []

n = len(list0)

for i in range(0, n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if(list0[i] + list0[j] + list0[k] == 0):
                all.append([list0[i],list0[j],list0[k]])

print(all)

# o/p : [[-10, 2, 8], [-7, -3, 10]]

# Working : 
# n = 8

# 1) i = 0 	till 6
# j = 1		till 7
# k = 2		till 8

# -25 - 10 -7

# 2) k = 3
# -25 - 10 - 3
# .......................

# i = 0
# j = 2
# k = 1

# CONTINUE LATER