class grandpa:
    def __init__(self):
        self.age = int(input('Enter age: '))

class dad:
    def __init__(self):
        self.dept = input('Enter dept: ')

class son:
    def __init__(self):
        self.name = input('Enter name: ')
        grandpa.__init__(self)
        dad.__init__(self)

    def print(p):
        print("")
        print(p.name)
        print(p.age)
        print(p.dept)

obj1 = son()

obj1.print()