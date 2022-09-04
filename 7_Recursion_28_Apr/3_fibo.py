def fibonacci(num):
    # print(num)
    if num <= 1:  # base case
        return num
    else:
        return fibonacci(num-1) + fibonacci(num-2) # imp
        
for i in range(5):  
    print(fibonacci(i),end=" ")

# o/p : 0 1 1 2 3



# Note: 
# 0 1 directly printed on fib(i=0,1) due to base case
# on i=2 stack tree starts, [can chk by changing to range(2,5)]
# fib(1) calculated for each branch separately, this disadvantage is later overcome in DP
# the rightmost branch fib(1) is executed last

# STACK TREE : 
# 1) Start from LEFTMOST bottom > fib(1) = 1 then move RIGHT to fib(0) = 0,
# 2) Add them to get 1 for fib(2), return & print result, then move to its ryt fib(1) = 1




# STACK MEMORY