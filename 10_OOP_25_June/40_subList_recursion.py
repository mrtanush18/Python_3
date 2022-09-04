# Print all combinations of list elements using recursion
# No class or Inheritance, Polymorphism, Composition needed as list has no attributes

def subs(list1):
    if list1 == []:
        return [[]]

    x = subs(list1[1:])

    return [[list1[0]] + y for y in x] + x

print (subs([4,5,6]))

# o/p : [[4, 5, 6], [4, 5], [4, 6], [4], [5, 6], [5], [6], []]

# 4 + [5,6] + [5,6]