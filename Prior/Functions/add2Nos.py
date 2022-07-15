x = int(input('Enter first number: '))
y = int(input('Enter second number: '))

def addTwoNos(a,b): # fn definition
    sum = 0
    sum = a + b
    return sum
    
result = addTwoNos(x,y)  # fn call

print(result) 

# o/p :
# Enter first number: 2
# Enter second number: 3
# 5
