# search phone, display details

class phone:
    def __init__(self):
        self.name = input('\nEnter name of phone: ')
        self.price = int(input('Enter price: '))
        self.mNo = input('Enter model no.: ')

    def showPhoneInfo(s):
        print(s.name)
        print(s.price)
        print(s.mNo)
  
list0 = []

while(1):
    ans = input('Add record? ')
    if ans == 'yes':
        n = int(input('How many? '))
        for i in range(n):
            temp = "phone" + str(i)
            list0.append(temp)
            list0[i] = phone()
            
    else:
        print("\nALL PHONES:")
        for i in range(n):
            list0[i].showPhoneInfo()
        break
    
    
    # print(list0)

    ans2 = input('Which phone model')
    for x in list0:
        if x.mNo == ans2:
            print(x.name)
            print(x.price)



'''
o/p:

'''