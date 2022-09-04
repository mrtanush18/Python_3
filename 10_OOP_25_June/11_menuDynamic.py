# 1. tea ; Rs. 50

class menu:
    def __init__(self):
        self.name = input('Enter name of food item: ')
        self.price = int(input('Enter price of food item: '))

    def showMenu(s,i):
        print(str(i+1),")",s.name,";", s.price)

    # def __del__(s):
    #     print('\n',s.name, "deleted")

list0 = []
n = 0

while(1):
    ans = input('Add to menu? ')
    if(ans == 'yes'):
        n = int(input('How many? '))
        for i in range(n):
            temp = 'food' + str(i)
            list0.append(temp)
            list0[i] = menu()
    else:
        break

# print(list0)


ans2 = input('Delete from menu? ')
if(ans2 == 'delete'):    
        m = int(input('How many? '))
        # if m < len(list0):
        for i in range(m):
            deleteObj = input('Which item to delete? ')
            if list0[i].name == deleteObj:
         
                list0.remove(list0[i])
    else:
        break

    #         else:
    #             print('Number exceeds list size')
    #     else:
    #         break
    # else:
    #     break

if len(list0) != 0: 
    print('\nMenu:')
    for i in range(len(list0)):
        list0[i].showMenu(i)

'''
____________________________________
> o/p:
____________________________________
Which item to delete? fries
Traceback (most recent call last):
  File "g:\My Drive\Py\OOP\11_menuDynamic.py", line 38, in <module>
    if i.name == deleteObj:
AttributeError: 'int' object has no attribute 'name'

'''