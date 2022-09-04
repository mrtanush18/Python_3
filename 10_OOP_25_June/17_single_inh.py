# Single Inheritance: 
# Single inheritance enables a derived class to inherit properties from a single parent class, 

class person:
    def __init__(self):
        self.name = input('Enter name ')
        self.id = input('Enter id ')
    
    def showValues(s):
        print("")
        print(s.name)
        print(s.id)
        print(s.salary) # printed child attributes here
        print(s.doj)

class emp (person):  # (parent class name) to indicate inheritance for compiler
    def __init__(self):
        self.salary = int(input('Enter salary '))
        self.doj = input('Enter date ')
        person.__init__(self)  # got to call parent constructor

# created object of child as child has got all properties of parent 

emp1 = emp()

emp1.showValues()

'''
o/p:

Enter salary 5000
Enter date 18/08/1999
Enter name tanush
Enter id 363011

tanush
363011
5000
18/08/1999

'''