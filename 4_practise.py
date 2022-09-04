def power(n,p):
    # if n == 0:
        # return 0
    if p == 1:
        return num
    else:
        return num * power(n,p-1)



num = 2
pow = 3

print(power(num,pow))