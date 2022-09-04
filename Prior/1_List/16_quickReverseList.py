# Reverse list using n/2 iterations & without using another list

list = [100,-56,5,6,7,8]
count = 0
j = -1

print('OG list: ',list)

# HOW TO SWAP LIST ELEMENTS

for i in range(len(list)//2):  # // : floor div operator to round to nearest whole no.
        temp = list[i] 
        list[i] = list[j] 
        list[j] = temp
        j = j - 1
        count = count + 1
        
print("Reversed list:",list)
print('\nNo. of iterations: ', count)

# o/p:
# OG list:  [100, -56, 5, 6, 7, 8]
# Reversed list: [8, 7, 6, 5, -56, 100]
# No. of iterations: 3

# TRACING:
# >> Original code snippet:
# j = -1
# list = [100,-56,5,6,7,8]
# for i in range(len(list)//2):
#       temp = list[i] 
#       list[i] = list[j] 
#       list[j] = temp
#       j = j - 1

# Iterations:
# for i in range(3):
#       temp = list[0] = 100
#       list[0] = list[-1] = 8
#       list[-1] = temp = 100
#       j = j - 1 = (-1 -1) = -2 

# [8,-56,5,6,7,100]

# for i in range(3):
#       temp = list[1] = -56
#       list[1] = list[-2] = 7
#       list[-2] = temp = -56
#       j = j - 1 = -2 -1 = -3 

# [8,7,5,6,-56,100]

# for i in range(3):
#       temp = list[2] = 5
#       list[2] = list[-3] = 6
#       list[-3] = temp = 5
#       j = j - 1 = -3 -1 = -4 

# [8,7,6,5,-56,100]