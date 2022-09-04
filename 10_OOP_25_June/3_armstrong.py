# 153 = 1*1*1 + 5*5*5 + 3*3*3

class armstrong:
    def __init__(self,number):
        self.number = number

    def chkArmstrong(n):
        n.sum = 0
        string = str(n.number)
        for i in range(len(string)):
            n.sum = n.sum + pow(int(string[i]),3)
        print(n.sum)
        if n.sum == n.number:
            print('Yes')
        else:
            print('No')


obj1 = armstrong(153)
obj2 = armstrong(152)

obj1.chkArmstrong()
obj2.chkArmstrong()

# o/p :
# Yes
# No