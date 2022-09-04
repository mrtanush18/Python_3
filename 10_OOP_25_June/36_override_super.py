# Overriding : Req 2 classes (inheritance)
# >> More than 1 method has the same name, number,& type of parameters.
# Used super fn in single inheritance
# https://www.geeksforgeeks.org/python-super/

class person:
    def __init__(self):
        self.name = input('Enter name ')
        self.id = input('Enter id ')
    
    def showValues(s):
        print("PARENT CLASS METHOD")
        print(s.salary)
        print(s.doj)

    def abtPerson(s):
        print(s.name)
        print(s.id)

class emp (person):  
    def __init__(self):
        self.salary = int(input('Enter salary '))
        self.doj = input('Enter date ')
        super().showValues()              # To call parent's showValue method

    def showValues(s):
        print("CHILD CLASS METHOD")
        print(s.salary)
        print(s.doj)

emp1 = emp()

# emp1.showValues()                           # To call child's showValue method, comment this to display parent's

# o/p:
# Enter salary 5000
# Enter date 13/08
# CHILD CLASS METHOD
# 5000
# 13/08


# o/p : [with super()]
# Enter salary 4000
# Enter date 18/08
# PARENT CLASS METHOD
# 4000
# 18/08
