# Hierarchical Inheritance: 
# When more than one derived class are created from a single base this type of inheritance is called hierarchical inheritance

class person:
    def __init__(self):
        self.name = input('Enter name ')
        self.age = int(input('Enter age ')) 
    
class carpenter(person):
    def __init__(self):
        print("Carpenter's details")
        self.salary = int(input('Enter salary '))
        person.__init__(self)
    
    def print2(p):
        print(p.name)
        print(p.age)
        print(p.salary)


class doctor(person):
    def __init__(self):
        print("Doctor's details")
        self.patients = int(input('Enter no. of patients '))
        person.__init__(self)

    def print3(p):
        print("Doctor's details")
        print(p.name)
        print(p.age)
        print(p.patients)

obj1 = carpenter()
obj2 = doctor()

obj1.print2()
obj2.print3()

'''
o/p:

Carpenter's details
Enter salary 200
Enter name raju
Enter age 20
Doctor's details
Enter no. of patients 10
Enter name michael
Enter age 34
raju
20
200
Doctor's details
michael
34
10

'''