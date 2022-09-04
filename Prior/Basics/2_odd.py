# input function by default returns string so we put int()

num = int(input("Plz enter a number "))

print("Datatype:", type(num))

if(num % 2 == 0):
    print(num, "is even")
else:
    print(num, "is odd")