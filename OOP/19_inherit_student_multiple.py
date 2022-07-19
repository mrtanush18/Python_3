# Multiple inhertitance ex

class personal:
    def __init__(self):
        self.id = input('Enter id: ')
        self.name = input('Enter name: ')
        self.gender = input('Enter gender: ')

    def x(s):
        print('hi')

class educational:
    def __init__(self):
        self.branch = input('Enter branch: ')
        self.yop = int(input('Enter year of passing: '))

class student (personal, educational):
    def __init__(self):
        self.address = input('Enter address: ')
        self.contact = int(input('Enter contact no.: '))
        personal.__init__(self)
        educational.__init__(self)

    def print(p):
        print("")
        print(p.id)
        print(p.name)
        print(p.gender)
        print(p.address)
        print(p.contact)
        print(p.branch)
        print(p.yop)

student1 = student()

student1.print()

student1.x()

'''
# o/p:

Enter address: midc andheri
Enter contact no.: 981
Enter id: 123
Enter name: sam
Enter gender: male
Enter branch: comps
Enter year of passing: 2022

123
sam
male
midc andheri
981
comps
2022
'''