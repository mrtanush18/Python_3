def fn1(x,y):
    if x == 0:    # base case, terminates program
        return y
    else:
        return fn1(x-1 , x+y)

print(fn1(5,2))

# o/p :  17

# STACK TREE : 
# 0 , 17, base case reached return y (17)
# 1 , 16 
# 2 , 14
# 3 , 11
# 4 , 7
# 5 , 2