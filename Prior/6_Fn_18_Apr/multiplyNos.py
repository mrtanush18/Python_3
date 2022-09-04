x = int(input())
y = int(input())
z = int(input())

def multiplyNos(a=1,b=1,c=1):  # default parameters, when no. of paramters is known
    product = 1

    product = product * a * b * c

    print("Product is ",product)

multiplyNos(7,2)

