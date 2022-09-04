# Abstract class implements abstraction, encourages inheritance in child classes

from abc import ABC, abstractmethod

class person(ABC):
    def __init__(self):
        self.name = input('Name?')
        self.age = int(input('Age?'))

    @abstractmethod
    def salary(s):
        pass

class doctor (person):
    def __init__(self):
        person.__init__(self)

    # def salary(s):
    #     print(5000)

class engineer (person):
    def __init__(self):
        person.__init__(self)

    def salary(s):
       print(10000)

obj3 = doctor()
obj3.salary()

'''
o/p:
File "g:\My Drive\Py\OOP\28_abstract_class.py", line 28, in <module>
    obj3 = doctor()
TypeError: Can't instantiate abstract class doctor with abstract method salary
'''
'''
____________________________________
NOTES :
____________________________________
Abstract class uses abstraction
Can we create object of abstract class, no as it is a concept, incomplete class
Abstract attributes make a abstract method in turn makes abstract class
When to use concrete class ? 
> when I know abt methods, attributes
Class doesn't use memory

'''