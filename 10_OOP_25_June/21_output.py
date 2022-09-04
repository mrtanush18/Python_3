# Guess o/p :

class a:
    def __init__(s, n='tanush'):
        s.__name = n      # private instance variable

class b (a):
    def __init__(s, roll_no):
        s.roll_no = roll_no
        a.__init__(s)

obj1 = b(50)

print(obj1.name)
print(obj1.roll_no)

'''
Traceback (most recent call last):
  File "g:\My Drive\Py\OOP\21_output.py", line 12, in <module>
    print(obj1.name)
AttributeError: 'b' object has no attribute 'name'
_______________________________________________________
# Commenting print(obj1.anme) results in o/p 50
'''