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
    print("")
    ans2 = input('Enter model no. to print details of phone: ')
    for x in list0:
        if x.mNo == ans2:
            print('')
            print('Search results:')
            print("Brand: ", x.name)
            print("Cost: ", x.price)



'''
o/p:

Add record? yes
How many? 2

Enter name of phone: samsung
Enter price: 6000
Enter model no.: s10

Enter name of phone: iphone
Enter price: 50000
Enter model no.: iphone_10

Enter model no. to print details of phone: s10

Search results:
Brand: samsung
Cost: 6000
Add record? no

ALL PHONES:
samsung
6000
s10
iphone
50000
iphone_10

'''