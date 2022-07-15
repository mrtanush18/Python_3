# Comparative operators can be used to compare between the object’s attributes. The available methods are __lt__, __gt__, __le__, __ge__, __eq__, and __ne__ that performs less than, greater than, less than or equal to, greater than or equal to, equal to, and not equal to operations respectively.

class Comparison:
    def __init__(self, a):
        self.a = a
    def __lt__(self, object2):
        return self.a < object2.a
    def __gt__(self, object2):
        return self.a > object2.a
    def __le__(self, object2):
        return self.a <= object2.a
    def __ge__(self, object2):
        return self.a >= object2.a
    def __eq__(self, object2):
        return self.a == object2.a
    def __ne__(self, object2):
        return self.a != object2.a
a = Comparison(1)
b = Comparison(2)
print(
    a < b,
    a > b,
    a <= b,
    a >= b,
    a == b,
    a != b
)
# Output
# True False True False False True