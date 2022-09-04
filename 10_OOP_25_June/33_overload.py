# Overloading : Req single class
# >> More than 1 method has the same name BUT with different no. OR type of parameters.              

class poly:
    def __init__(self):
        print('Polymorphism')

    def ar1(s,a):
        print(a)

    def ar2(s,a,b):
        print(a+b)

    def ar3(s,a,b,c):
        print(a+b+c)


obj1 = poly()

obj1.ar1(17)
obj1.ar2(1,2)
obj1.ar3(1,2,3)

# '''
# o/p:
# Polymorphism
# 17
# 3 
# 6
# '''