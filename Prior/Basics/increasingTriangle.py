n = 5
for i in range(n):            # start with row 'i' = 0
    for j in range(i+1):        # start with col 'j' = 1 as 1 star on row 0
        print('*', end=" ")   
    print() 

# O/P :
# * 
# * * 
# * * *
# * * * *
# * * * * *

# DECREASING TRIANGLE : 
# n = 5
# for i in range(n):            # start with row 'i' = 0
#     for j in range(i,n):        # start condition col 'j' = i = 0 and print till n
#         print('*', end=" ")   
#     print()

# O/P :
# * * * * * 
# * * * * 
# * * *
# * *
# *

# Working :
# i = 0  * * * * *       j = 0 1 2 3 4  (0 to 5)
# i = 1  * * * *         j = 1 2 3 4    (1 to 5)
# i = 2  * * *           j = 2 3 4      (2 to 5)
# i = 3  * *             j = 3 4        (3 to 5)
# i = 4  *               j = 4          (4 to 5)