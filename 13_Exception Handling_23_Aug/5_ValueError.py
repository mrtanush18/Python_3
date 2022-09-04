try:
    while(1):
        n = int(input('Enter +ve number '))
        if(n > 0):
            print(pow(n,2))
        else:
            raise ValueError('-ve number not valid')
except ValueError as obj1:
    print(obj1.args)

















# n = int(input('Enter +ve number '))

# if(n > 0):
#     while(1):
#         n = int(input('Enter +ve number '))
# else:
#     raise ValueError('-ve number not valid')