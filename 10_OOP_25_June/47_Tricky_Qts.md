
> Quiz 1 : https://www.techbeamers.com/online-python-quiz-beginners-classes-objects/
+ Q6 : Use self
ex.
def __init__(self):
    self.id = 10
    id = 10 >> (WRONG)

+ Q9 : __dict__ 

+ Q10 : invoke parent class from child class

+ Q11 : child class does not inherit parent class attribute as parent constr not called
Hence call super().__init__() from child class constr

+ Q13 : On calling parent constr from child class, self refers to child class

+ Q15 : isInstance(objName,className) : chks if object belongs to a class or not

> Quiz 2 : https://www.techbeamers.com/python-online-quiz-experienced/
+ Q2 : calling constructor (creating object) without passing arguments results in error

+ Q6 : val.x = 45 is example of overriding public variable of class Test
In function just default values of fn is given to avoid error if no arguments are passed

+ Q7 : private data field : self.__b = 1  (double underscore)

+ q10 : super().__init__() or __init__(self)

+ q12 : super().init() from another class will result in parent class values getting printed. Hence self.__x = 1 , 1 will get printed

+ q13 : main > class B > override with x = 3 & y gets incremented by 1 when increment fn is called

+ q14 : Line self.__init__(self) is imp. Here __new__ fn is called when object gets created. 
> __new__ method creates instance if object internally & passes it to __init__

+ q15 : b class has no attribute x error as no inheritance as parent constructor not called

+ q19 : In function just default values of fn is given to avoid error if no arguments are passed
> == is example of operator overloading
In return self.x * self.y == num.x * num.y 
a is self & b is num, so in a , value of x is 1, y = 2 and vica versa in b so product is same both sides

+ q21 : Anonymous objects is used here : 

def main():
    A().printInfo()
    B().printInfo()

Hence object gets created only for class A & in o/p it prints 2 times A’s getInfo is called

