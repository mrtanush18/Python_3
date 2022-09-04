class division:
    def __init__(self):
        self.x = input('Enter no1 ')
        self.y = input('Enter no2 ')

    def divide(s):
        try:
            s.result = (int(s.x) // float(s.y))
        except ZeroDivisionError:
            print('Plz enter other value than 0')
        else:
            print(s.result)        

obj1 = division()
obj1.divide()

# o/p : 
# Enter no1 2
# Enter no2 0
# Plz enter other value than 0