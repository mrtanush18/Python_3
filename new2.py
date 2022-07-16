class parent1:
    def __init__(self):
        self.str1 = input('Enter a word 1 ')
        print('parent1')

class parent2:
    def __init__(self):
        self.str2 = input('Enter a word 2 ')
        print('parent2')

class child (parent1, parent2):
    def __init__(self):
        parent1.__init__(self)
        parent2.__init__(self)

    def print(p):
        print("")
        print(p.str1)
        print(p.str2)


obj1 = child()

obj1.print()