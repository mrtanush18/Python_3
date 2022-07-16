class person:
    def __init__(self):
        self.name = input('Enter name ')
        self.id = input('Enter id ')
    
    def showValues(s):
        print('\n',s.name)
        print(s.id)
        print(s.salary)
        print(s.doj)

class emp (person):
    def __init__(self):
        self.salary = int(input('Enter salary '))
        self.doj = input('Enter date ')
        person.__init__(self)

emp1 = emp()

emp1.showValues()