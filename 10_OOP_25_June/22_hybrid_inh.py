# Hybrid Inheritance

class university:
    def __init__(self):
        self.region = input('enter region of uni ')

    def display(s):
        print(s.region)

class course (university):
    def __init__(self):
        self.grade = input('enter grade of university ')

    def display(s):
        print(s.grade)
        university.display(s)

class branch (university):
    def __init__(self):
        self.type2 = input('enter your branch ')

    def display(s):
        print(s.type2)
        university.display(s)

class student (course, branch):
    def __init__(self):
        self.roll_no = int(input('enter roll no '))
        university.__init__(self)
        course.__init__(self)
        branch.__init__(self)

    def display(s):
        print(s.roll_no)
        branch.display(s)
        course.display(s)

obj1 = student()

obj1.display()

'''
o/p:
enter roll no 10
enter region of uni mumbai
enter grade of university A
enter your branch comps
10
comps
mumbai
A
mumbai
'''