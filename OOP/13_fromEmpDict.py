# Take i/p from dict and print emp name using oop

class employee:
    def __init__(self,name,dept,age):
        self.empName = name
        self.empDept = dept
        self.empAge = age

    def showDetails(s):
        print("\nAll details:")
        print("Name: ",s.empName)
        print("Dept: ",s.empDept)
        print("Age: ",s.empAge)

dict1 = {'name':'ram', 'dept' : 'it', 'age' : 27}

emp1 = employee(dict1['name'],dict1['dept'],dict1['age'])

emp1.showDetails()

'''
o/p:

All details:
Name:  ram
Dept:  it
Age:  27

'''
