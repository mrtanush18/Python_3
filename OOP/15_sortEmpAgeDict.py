# Display emp details in dictionary sorted by age, (to sort name, have to display separate o/p)

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

list0 = []

emp1 = emp()
emp2 = emp()
emp3 = emp()

list0.append(emp1)
list0.append(emp2)
list0.append(emp3)

age = []

for i in list0:
    age.append(i.empAge)    

# print(age)

age.sort()
print(age)

for j in age:
    for i in list0:
        if i.empAge == j:
            i.showDetails()
            continue

'''
o/p : 
Enter name sam
Enter department it
Enter age 23
Enter name ram
Enter department hr
Enter age 20
Enter name shyam
Enter department sales
Enter age 45
[20, 23, 45]

All details:
{'name': 'ram', 'dept': 'hr', 'age': 20}

All details:
{'name': 'sam', 'dept': 'it', 'age': 23}

All details:
{'name': 'shyam', 'dept': 'sales', 'age': 45}
'''