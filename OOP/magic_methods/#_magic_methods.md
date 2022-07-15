operator overloading,

1) __new__() method
Languages such as Java and C# use the new operator to create a new instance of a class.
In Python the __new__() magic method is implicitly called before the __init__() method. The __new__() method returns a new object, which is then initialized by __init__().

