class employee:
    def __init__(self):
        self.name = input('Enter name ')
        print(self.name, " is created")

    def __delete__(self):
        print('\n',self.name, " is deleted")


obj1 = employee()
obj2 = employee()
obj3 = employee()

del obj1
# del obj2

'''
o/p:

Enter name sam
sam  is created
Enter name ram 
ram  is created

sam  is deleted
ram  is deleted
'''