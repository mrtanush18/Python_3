# o/p : sq(1) - sq(2) = -3
# sq(1) + sq(2) - 3 = 2
# sq(all nos)/5  = 11

class arithmetic:
    def __init__(self,*arg):
        self.list0 = []
        print("*arg: ",*arg)
        for value in arg:
            self.list0.append(value)

        # print(self.list0)

    def two(s):
        s.sum = 0
        for item in s.list0:
            s.sum = -pow(item,2) - s.sum
        print(s.sum)    

    def three(s):
        s.sum = 0
        for i in range(len(s.list0)-1):
            s.sum = pow(s.list0[i],2) + s.sum
        print(s.sum-s.list0[-1]) 

    def five(s):
        s.sum = 0
        for i in range(len(s.list0)):
            s.sum = pow(s.list0[i],2) + s.sum
        print(s.sum//s.list0[-1])         

    
    def call(s):
        if len(s.list0) == 2:
            s.two()
        if len(s.list0) == 3:
            s.three()
        if len(s.list0) == 5:
            s.five()


obj1 = arithmetic(1,2)
obj2 = arithmetic(1,2,3)
obj3 = arithmetic(1,2,3,4,5)


obj1.call()
obj2.call()
obj3.call()

'''
o/p:
*arg:  1 2
*arg:  1 2 3
*arg:  1 2 3 4 5
-3
2
11
'''










