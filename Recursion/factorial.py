# factorial
def fact(num):
    if num <= 1:   # terminating condition
        return num
    else:
        return num * fact(num-1)  # num value keeps getting stored in stack frame till num<=1


print(fact(5))

# o/p : 120

# STACK TREE : 

# 1 * fact(0) = 1    0! = 1
# 2 * fact(1) = 2    1! = 1
# 3 * fact(2) = 6    2! = 2
# 4 * fact(3) = 24   3! = 6
# 5 * fact(4) = 120  4! = 24
