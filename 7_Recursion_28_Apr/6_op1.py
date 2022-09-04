# find o/p

def fn1(n):
    if n == 0:
        return n
    
    fn1(n//2)
    print(n%2, end=" ")


fn1(21)

# o/p : 1 0 1 0 1 

# 1/2 = 0 return 1
# 2/2 = 1 
# 5/2 = 2
# 10 / 2 = 5
# 21/2 = 10