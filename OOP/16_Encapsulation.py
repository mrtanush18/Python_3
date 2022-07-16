# Encapsulation is not very tight in Python 3, may change in newer versions

class counter:
    def __init__(self):
        self.__current = 0
    def increment(s):
        s.__current = s.__current + 1
    def show(f):
        print(f.__current)
    def reset(z):
        z.__current = 0

obj1 = counter()
obj2 = counter()
obj1.increment()
obj1.increment()
obj1.increment()
obj1.show()

# access private attribute from outside
print(obj1._counter__current)

# modify private attribute from outside
obj1.current = -10
print(obj1.current)

# print(obj2.current)

# o/p :  
# 3
# 3
# -10