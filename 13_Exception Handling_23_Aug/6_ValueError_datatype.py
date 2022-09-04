# If I enter string, program should keep running, if number it should end

while(1):
    try:
        n = int(input('Enter +ve number: '))
        if type(n) == int:
            print(n)
            break

    except ValueError as obj1:
        print('ValueError, enter number')


















# n = int(input('Enter +ve number '))

# if(n > 0):
#     while(1):
#         n = int(input('Enter +ve number '))
# else:
#     raise ValueError('-ve number not valid')