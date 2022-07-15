def sumOfFirst10():  
    sum = 0   # written inside fn, local variable
    for i in range(11):
        sum = sum + i
    # print(sum)
    return sum

# sumOfFirst10()

x = sumOfFirst10()

print(x)


