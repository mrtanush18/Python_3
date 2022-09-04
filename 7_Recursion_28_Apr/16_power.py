# calc power of a number using recursion

def calcPower(num,pow):
    if(num == 0):
        return 0
    if(pow == 1):  # 1
        return num

    return(num * calcPower(num,pow-1))  # brackets to resolve error

num = 2
pow = 3

print(calcPower(num,pow))

# O/P : 8 (num=2, pow=3)

# STACK TREE :
# 4 * 2 = 8 pow = 1 base case reached return num = 8
# 2 * 2 = 4 pow = 2

