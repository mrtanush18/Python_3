# __iter__ magic method
# __iter__ method is used to provide a generator object for the provided instance. We can make use of iter() and next() method to leverage __iter__ method.

class Squares:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
    def __iter__(self):
        for value in range(self.start, self.stop + 1):
            yield value ** 2
i = iter(Squares(1, 3))
print(next(i))
print(next(i))
print(next(i))

# Output: 1 4 9

# In the code above we are going to find the squares of the values between the provided range (start and stop). When we invoke the method iter(Squares(1, 3)) the __iter__ method is invoked which is a method that yields squares of the values between the provided range. In our example, we use the range from 1 to 3 so the output would be 1, 4, and 9 if we invoke the next() method.