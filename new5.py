class a:
    def __init__(s, n='tanush'):
        s.__name = n

class b (a):
    def __init__(s, roll_no):
        s.roll_no = roll_no
        a.__init__(s)

obj1 = b(50)

print(obj1.name)
print(obj1.roll_no)

