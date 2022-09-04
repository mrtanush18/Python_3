class multi2:
    def exceptions(s):
        try:
            n = 0
            m = 2
            c = m/n
        except(ZeroDivisionError) as e:
            print("Cannot divide by zero")
        try:
            n = 2
            m = '3'
            p = m+n
        except TypeError:
            print('Both numbers must be in string format')

obj1 = multi2()
obj1.exceptions()