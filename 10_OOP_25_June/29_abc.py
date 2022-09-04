from abc import ABC, abstractmethod # ABC : Abstract Base class

class dog(ABC):
    def __init__(self):
        self.size = input('Large/Small?')
        self.age = int(input('Age?'))

    @abstractmethod  # decorator / annotation in spring
    def cost(s):
        pass

class poodle (dog):
    def __init__(self):
        print('Poodle')
        dog.__init__(self)

    def cost(s):
        s.cost = input('Çost of keeping poodle?')


class retriever (dog):
    def __init__(self):
        dog.__init__(self)
    
    def cost(s):
        s.cost = input('Çost of keeping retiever?')

pet1 = poodle()
pet2 = retriever()


pet1.cost()
pet2.cost()

'''
o/p:

Poodle
Large/Small?small
Age?2
Large/Small?large
Age?4
Çost of keeping poodle?2000
Çost of keeping retiever?4000
'''