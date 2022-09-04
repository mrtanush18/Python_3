# Composition "has a"

class component: # engine
    def __init__(self):
        print("Component class obj created")

    def m1(p):
        print('Component class method executed')

class composite: # car
    def __init__(self):
        print("Composite class obj created")
        self.obj1 = component()

    def m2(self):
        self.obj1.m1()

obj2 = composite()

obj2.m2()

'''
# o/p :
Composite class obj created
Component class obj created
Component class method executed
'''