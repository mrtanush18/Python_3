class threeObj:
    def setValues(s0):
        s0.first = int(input('Enter first no.: '))
        s0.second = int(input('Enter second no.: '))
    
    def __add__(self,a):        # magic method #1 self = obj1, a = obj2 >> #2 self = previous sum
        # obj = threeObj()
        self.first = self.first + a.first    # obj1 + obj2 >> # self.first + obj3.first
        self.second = self.second + a.second
        return self

    def printSum(self):
        print("Sum of first nos: ",self.first,",Sum of second nos: ",self.second,"& sum=",(self.first + self.second))

list0 = []
count1 = 0
while(1):
    ans = input('Add number? ')
    if ans == 'yes':
        n = int(input('How many pairs of nos? '))
        for i in range(n):
            count1 = count1 + 1
            list0.append(threeObj())
            list0[i].setValues()
    break
print("No. of objects created: ",count1)

# print(list0)
# sumObj = 0
# count = 0

sumObj = threeObj()
sumObj.first = 0
sumObj.second = 0

for i in range(n):  
    sumObj = sumObj + list0[i]

sumObj.printSum()

# sumObj = list0[0] + list0[1] + list0[2]
# sumObj.printSum()


'''
o/p:
Add number?yes
How many pairs of nos? 3
Enter first no.: 10
Enter second no.: 20
Enter first no.: 10
Enter second no.: 20
Enter first no.: 20
Enter second no.: 30
No. of objects created: 3
Sum of first nos: 40, Sum of second nos: 70 & sum= 110

'''