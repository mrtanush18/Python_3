# __contains__ magic method
# __contains__ method is invoked when using the membership operator ‘in’. When we want to check whether an element is present in the object’s attributes that are usually container (lists, tuple) we can use the __contains__ method.

class ContainsExample:
    def __init__(self, items):
        self.items = items
        
    def __contains__(self, item):
        return item in self.items
contains_instance = ContainsExample([1, 2, 3, 4, 5])
print(4 in contains_instance)

# o/p : true

# The above code uses __contains__ method to find whether an integer is present in the list of integers. In the code above we checked whether the integer 4 is present in the list of integers that is an attribute of the class Contains