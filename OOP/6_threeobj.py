class threeObj:
    sum = 0
    total1 = 0
    total2 = 0
    total3 = 0
    
    def __init__(s):
        s.first = 0
        s.second = 0

    def input(s0):
        s0.first = int(input('Enter first no.: '))
        s0.second = int(input('Enter second no.: '))
    
    def add(s1):
        threeObj.sum = s1.first + s1.second
        threeObj.total1 = threeObj.total1 + s1.first
        threeObj.total2 = threeObj.total2 + s1.second
        threeObj.total3 = threeObj.total1 + threeObj.total2

    @staticmethod
    def printSum():
        print(threeObj.sum)

    @staticmethod
    def printTotal():
        print("sum of all firsts: ",threeObj.total1)
        print("sum all seconds: ",threeObj.total2)
        print("sum all firsts & seconds: ",threeObj.total3)
   

obj1 = threeObj()
obj2 = threeObj()
obj3 = threeObj()

obj1.input()
obj1.add()
obj1.printSum()

obj2.input()
obj2.add()
obj2.printSum()

obj3.input()
obj3.add()
obj3.printSum()

threeObj.printTotal()

'''
o/p:
Enter first no.: 10
Enter second no.: 20
30
Enter first no.: 20
Enter second no.: 30
50
Enter first no.: 40
Enter second no.: 50
90
sum of all firsts:  70
sum all seconds:  100
sum all firsts & seconds:  170
'''