# o/p : sum of list : 15
# sq of int : 25
# string : "python programming"

class x:
    def __init__(self,a):
        if type(a) == list:
            print("Sum of list: ",sum(a))
        if type(a) == int:
            print("Square of int: ", pow(a,2))
        if type(a) == str:
            print("String: ",a + " programming")

obj1 = x([1,2,3,4,5])
obj2 = x(5)
obj3 = x("python")

'''
o/p:
Sum of list:  15
Square of int:  25
String:  python programming
'''