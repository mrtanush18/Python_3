# print:
# 1. name, price , model no. of phone1
# 2. name, price , model no. of phone2
# ....

class phone:
    def __init__(self):
        self.name = input('\nEnter name of phone: ')
        self.price = int(input('Enter price: '))
        self.mNo = input('Enter model no.: ')

    def showPhoneInfo(s):
        print(s.name)
        print(s.price)
        print(s.mNo)

    @staticmethod
    def searchPhone():
        ans2 = input('Which phone')
        for i in range(n):
            if ans2 == list0[i]:
                print(list0[i])
  
list0 = []

while(1):
    ans = input('Add record? ')
    if ans == 'yes':
        n = int(input('How many? '))
        for i in range(n):
            temp = "phone" + str(i)
            list0.append(temp)
            list0[i] = phone()
            # print(list0[i])
            
    else:
        print("\nALL PHONES:")
        for i in range(n):
            list0[i].showPhoneInfo()

        # list0[i].searchPhone()
        break



'''
o/p:

Add record? yes
How many? 2

Enter name of phone: samsung
Enter price: 4000
Enter model no.: s12

Enter name of phone: iphone
Enter price: 5000
Enter model no.: 10
Add record? no

ALL PHONES:
samsung
4000
s12
iphone
5000
10
'''