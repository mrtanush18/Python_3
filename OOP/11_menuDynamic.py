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

while(1):
    ans = input('Ádd to menu? ')
    if(ans == 'yes'):
        n = int(input('How many? '))
        for i in range(n):
            temp = 'food' + str(i)
            list0.append(temp)
            list0[i] = menu()
    else:
        print('\nMenu:')
        for i in range(n):
            list0[i].showMenu(i)
        break

print(list0)
ans2 = input('Delete from menu? ')
if(ans2 == 'yes'):    
    deleteObj = input('Which item to delete? ')
    for x in list0:
        if x.name == deleteObj:
            # del x.name
            print(x.name)
            list0.remove(x.name)
else:
    for i in range(n):
        print('else')
        list0[i].showMenu(i)
        break
