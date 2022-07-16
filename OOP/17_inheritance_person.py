# Simple inheritance

class person:
    def __init__(self):
        self.name = input('Enter name ')
        self.id = input('Enter id ')
    
    def showValues(s):
        print('\n',s.name)
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