class emp:
    def __init__(self):
        self.empName = input('Enter name ')
        self.empDept = input('Enter department ')
        self.empAge = int(input('Enter age '))

    def showDetails(s):
        print("\nAll details:")
        s.dict1 = {}
        s.dict1['name'] = s.empName
        s.dict1['dept'] = s.empDept
        s.dict1['age'] = s.empAge

        print(s.dict1)


emp1 = emp()

emp1.showDetails()


