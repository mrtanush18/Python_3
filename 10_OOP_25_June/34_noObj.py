# call class without creating object using @ classmethod decorator
# Instead of accepting a self parameter, class methods take a cls parameter that points to the class—and not the object instance—when the method is called.

class arithmetic:
    @classmethod
    def two(s,list0):
        # print(list0)
        sum = 0
        for item in list0:
            sum = - pow(item,2) - sum
        print(sum)    
    
    @classmethod
    def three(s,list0):
        sum = 0
        for i in range(len(list0)-1):
            sum = pow(list0[i],2) + sum
        print(sum-list0[-1]) 

    @classmethod
    def five(s,list0):
        sum = 0
        for i in range(len(list0)):
            sum = pow(list0[i],2) + sum
        print(sum//list0[-1])         

    @classmethod
    def call(s,list0):
        if len(list0) == 2:
            arithmetic.two(list0)
        if len(list0) == 3:
            arithmetic.three(list0)
        if len(list0) == 5:
            arithmetic.five(list0)

list0 = [[1,2],[1,2,3],[1,2,3,4,5]]

for i in range(len(list0)):
    arithmetic.call(list0[i])