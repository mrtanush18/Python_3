# Multilevel Inheritance :
# In multilevel inheritance, features of the base class and the derived class are further inherited into the new derived class.

class grandpa:
    def __init__(self):
        self.age = int(input('Enter age: '))

    def x(s):
        print('hi')

class dad (grandpa):
    def __init__(self):
        self.dept = input('Enter dept: ')

class son (dad):
    def __init__(self):
        self.name = input('Enter name: ')
        grandpa.__init__(self)
        dad.__init__(self)

    def print(p):
        print("")
        print(p.name)
        print(p.age)
        print(p.dept)

obj1 = son()        # created only son class's object as it inherits all methods, attributes

obj1.print()

obj1.x()

'''
o/p:
Enter name: tanush
Enter age: 22
Enter dept: IT  

tanush
22
IT
hi

'''