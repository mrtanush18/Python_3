# Hierarchical Inheritance: 
# When more than one derived class are created from a single base this type of inheritance is called hierarchical inheritance

class person:
    def __init__(self):
        self.name = input('Enter name')
        self.age = int(input('Enter age')) 
    
class carpenter(person):
    def __init__(self):
        self.salary = int(input('Enter salary'))
        person.__init__(self)
    
    def print2(p):
        print(p.name)
        print(p.age)
        print(p.salary)


class doctor(person):
    def __init__(self):
        self.patients = int(input('Enter no. of patients'))
        person.__init__(self)

    def print3(p):
        print(p.name)
        print(p.age)
        print(p.patients)

obj1 = carpenter()
obj2 = doctor()

obj1.print2()
obj2.print3()