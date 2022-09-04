# Abstract attributes : not giving value in parent method, give value in child method

from abc import ABC, abstractmethod

class shape(ABC):
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

    @property
    @abstractmethod         # get value
    def leng(s):
        pass

    @leng.setter
    @abstractmethod     # set value
    def leng(s):
        pass

    @property
    @abstractmethod     # get value
    def bread(s):
        pass


    @bread.setter  # set value
    @abstractmethod
    def bread(s):
        pass

    @abstractmethod
    def getArea(s):
        pass

    def printArea(p):
        print(p.area)

class rectangle(shape):
    def __init__(self,length,breadth):
        print('Rectangle')
        self.length = length
        self.breadth = breadth
        shape.__init__(self,length,breadth)

    # def _init_(self):
    #     print('Constr 2')

    # def _init_(self):   # overrides
    #     print('Constr 3')

    @property
    def leng(s):
        return s.length

    @leng.setter
    def leng(s):
        s.length = 60

    @property
    def bread(s):
        return s.breadth

    @bread.setter     
    def bread(s):
        s.breadth = 70


    def getArea(s):
        s.area = s.length * s.breadth


# class triangle(shape):
#     def _init_(self):
#         print('Triangle')
#         shape._init_(self)

#     def getArea(s):
#         s.area = (s.length * s.breadth)//2
        

shape1 = rectangle(40,50)
# shape2 = triangle()

shape1.getArea()
# shape2.getArea()

shape1.printArea()
# shape2.printArea()

'''
# o/p:
# Rectangle
# 2000
'''