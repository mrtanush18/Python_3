import math

class multi3:
    def exceptions(s):
        integers = ['orange',6,-8,'apple']
        for number in integers:
            try:
                number_factorial = math.factorial(number)
            except TypeError:
                print("The input is not supported.")
            except ValueError:
                print( number," is not a positive integer.")

obj1 = multi3()
obj1.exceptions()