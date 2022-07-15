# 1. tea ; Rs. 50

class menu:
    def __init__(self):
        self.name = input('Enter name of food item: ')
        self.price = int(input('Enter price of food item: '))

    def showMenu(s):
        print("\n",s.name,";", s.price)

    # def __del__(s): # deletes both objects when they are not in use (garbage collector)
    #     print("deleted")

food1 = menu()
food2 = menu()
food3 = menu()

list0 = []

list0.append(food1)
list0.append(food2)
list0.append(food3)

list0[0].showMenu()
list0[1].showMenu()
list0[2].showMenu()

# Delete name, price

ans2 = input('Delete from menu? ')
if(ans2 == 'yes'):    
    deleteObj = input('Which item to delete? ')


    for i in list0:
        if i.name == deleteObj:
            list0.remove(i)

for i in list0:
    print(i.name,";", i.price)

# Update name, price

ans3 = input('Update from menu? ')
if(ans3 == 'yes'):    
    updateObj = input('Which item to update? ')
    updateAttr = input('Which attribute to update? ')

    for i in list0:
        if i.name == updateObj:
            if 'name' == updateAttr:
                updatedName = input('Enter new name ')
                i.name = updatedName
            if 'price' == updateAttr:
                updatedPrice = int(input('Enter new price '))
                i.price = updatedPrice

for i in list0:
    print(i.name,";", i.price)

