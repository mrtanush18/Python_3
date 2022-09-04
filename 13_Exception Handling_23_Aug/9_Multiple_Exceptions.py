class multi:
    def Exception(s,n1):
        list0 = [0,1]
        for i in range(len(n1)): # General exception
            try:
                print(list0[n1])
            except:
                print('GE: Value of i must be integer not string')

        if type(n1) == str:
            try: # Type exception
                for i in range(len(str)):
                    print(str[i])
            except TypeError:
                print('TE')

        if type(n1) == int or type(n1) == float:
            ans = input('Division?')
            if ans == 'yes':
                s.n2 = int(input('Enter num to divide by n1'))
                if s.n2 == 0:
                    try:
                        s.ans = int(n1) // s.n2
                    except ZeroDivisionError:
                        print('ZE')

        if type(n1) == dict:
            findKey = input('Enter key to find')

            try:
                for k in n1.keys():
                    if findKey == k:
                        print('Found key')
            except KeyError:
                print('Key not found')
                

obj1 = multi()
obj1.Exception('1')
