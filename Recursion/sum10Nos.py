# Recursion

def sum1st10Nos(num):
    if(num<=1):
        return num
    else:
        return num + sum1st10Nos(num-1) 
        

print(sum1st10Nos(10))

# o/p : 55   (num = 10)

# STACK TREE : 
# 54 + 1 = 55
# 52 + 2 = 54
# 49 + 3 = 52
# 45 + 4 = 49
# 40 + 5 = 45
# 34 + 6 = 40
# 27 + 7 = 34
# 19 + 8 = 27
# 10 + 9 = 19