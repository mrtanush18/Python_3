class employee:
    def __init__(self):
        self.name = input('Enter name ')
        print(self.name, " is created")

    def __del__(self):
        print("")
        print(self.name, " is deleted")

obj1 = employee()
obj2 = employee()
obj3 = employee()

del obj1
del obj2

'''
o/p:

Enter name ram
ram  is created
Enter name sam
sam  is created
Enter name shyam
shyam  is created

ram  is deleted

sam  is deleted

shyam  is deleted  # as obj1.name, obj2.name, obj3.name all point to  self.name
'''