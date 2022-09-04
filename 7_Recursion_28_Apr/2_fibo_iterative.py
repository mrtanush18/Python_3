# display fibonacci series : 0 1 1 2 3 5

def fibonacci(num):                
    i = 0                 
    j = 1
    temp = 0  
    count = 0   # 4 variables

    for count in range(num):
        print(i, end = " ")
        temp = i + j
        i = j
        j = temp

fibonacci(5)

# o/p : 0 1 1 2 3 

# dry run :
# count = 0
# initialized i = 0  j = 1  temp = 0  

# print i = 0  

# count = 1
# temp = 1  i = 1  j = 1    

# print i = 1

# count = 2
# temp = 2  i = 1  j = 2

# print i = 1

# count = 3
# temp = 3  i = 2  j = 3

# print i = 2

# >> count = 4
# temp = 5  i = 3  j = 5

# print i = 3

