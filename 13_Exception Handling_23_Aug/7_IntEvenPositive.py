class onlyEven:
    def __init__(self):
        self.nos = [1,2,1.2,'a']
    def chkTypeValue(s):
        for i in s.nos:
            try:
                if isinstance(i,int):
                    print(i)
                else:
                    raise TypeError('error')
            except TypeError:
                print('Value of i must be integer not string')

    def chkEven(s):
        print('\nCHECKING FOR EVEN')
        for i in s.nos:
            try:
                if(type(i) == int):
                    if(i % 2 == 0):
                        print(i)
                    else:
                        raise ValueError()
            except ValueError:
                print('ValueError : Enter even positive number')

obj1 = onlyEven()
obj1.chkTypeValue()
obj1.chkEven()