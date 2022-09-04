class threeObj:
    sum = 0
    total1 = 0
    total2 = 0
    total3 = 0
    
    def setValue(s0):
        s0.first = int(input('Enter first no.: '))
        s0.second = int(input('Enter second no.: '))
    
    def __add__(self,a):        # magic method #1 self = obj1, a = obj2 >> #2 self = previous sum
        obj = threeObj()
        obj.first = self.first + a.first    # obj1 + obj2 >> # self.first + obj3.first
        obj.second = self.second + a.second
        return obj

    def printSum(self):
        print(self.first,self.second,"sum=",(self.first + self.second))


obj1 = threeObj()
obj2 = threeObj()
obj3 = threeObj()

print("obj1")
obj1.setValue()

print("obj2")
obj2.setValue()

print("obj3")
obj3.setValue()

sumObj = obj1 + obj2 + obj3  # + operator adds obj in front and behind it

print("Values: ")
print("obj1",end=" ")
obj1.printSum()

print("obj2",end=" ")
obj2.printSum()

print("obj3",end=" ")
obj3.printSum()

print("sumObj",end=" ")
sumObj.printSum()

'''
o/p:

obj1
Enter first no.: 20
Enter second no.: 30

obj2
Enter first no.: 50
Enter second no.: 40

obj3
Enter first no.: 10
Enter second no.: 20

Values:
obj1 20 30 sum= 50
obj2 50 40 sum= 90
obj3 10 20 sum= 30

sumObj 80 90 sum= 170
'''