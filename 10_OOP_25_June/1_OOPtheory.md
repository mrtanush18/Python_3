+ OOP replaces earlier procedural programming. OOP represents real world entities as classes with data & behaviour (properties & methods)

+ Problem in procedural programming that oop aims to fix: Any fn can access or modify global variables

+ In procedural programming, program is divided into small parts called functions.

> Importance of fns :
1) To simplify testing, 
ex. login button we want for 30 pages, we can write in one file, & call from other files so that if any error can easily identify. To call from other file,  import file as module

2) Reusability : We don't have to copy paste code repeatedly, can simply call function from 99 other pgs

+ Can send any no. of parameters using **arg (pointer) to a function, in python only.
_________________________________________________________________________________________________
# Pillars of OOP : 
_________________________________________________________________________________________________
> There are five essential or key features of object-oriented programming : classes and objects, inheritance, polymorphism, data abstraction, and encapsulation. 
Inheritance is the ability of one class to inherit the properties of another base class. 
Polymorphism facilitates using the same function with different aliases. 
Encapsulation and abstraction enable the simplicity of coding for developers where they only interact with a subset of an object's overall attributes, i.e., only what is essentially required.
_________________________________________________________________________________________________
>1) Abstraction : 
+ Simplifying behavior of object or abstracting what object does.
+ To show user only whats needed for current problem scenario. (hide complexity)
+ user =  program , variables = relevant attributes
+ Why? :To hide sensitive info from other classes,
Ex. student class can't access salary variable/attribute/data from teacher class if set to private
+ Also, so that max classes (users) can use it & not be overwhelmed. ex. if no os less users can use comp
___________________________________________________________________________________________________
>2) Encapsulation : 
+ Combine variables & methods into a single unit called class to prevent data from direct modification is called encapsulation. 

+ It is simply hiding the implementation complexity from the user of the object. The user of the object just needs to know the method name to get a behaviour / functionality

+ Hence, creating class is an ex. of encapsulation
+ In Python, we denote private attributes using underscore as the prefix i.e single _ or double __

+ API : public variables & methods of a class
+ model is DB, controller handles requests , and view is whats visibale on screen
___________________________________________________________________________________________________
>3) Inheritance :  
+ Inheritance is extending the implementation of a base class by creating a derived class that will provide a specialized functionality in addition to the existing one in base class.
Used for code reusability, where child (sub) class can use properties of the parent (base) class.
# Types : multilevel, multiple, hierarchical
___________________________________________________________________________________________________
>4) Polymorphism : 
means using the multiple implementation with same name. Types: overloading & overriding
+ Overloading (compile time) : same method name used in same class with different parameters / return type.
+ Overriding : derived classes can implement their version for the same method in the base class.

+ Operator overloading : ex. + can be used to add numbers or concat strings or add objects using __add__, one operator, different uses

___________________________________________________________________________________________________
 [Press Alt + Z to read better]
___________________________________________________________________________________________________
 	                       Method Overloading                     Method Overriding
___________________________________________________________________________________________________                       
>1) Invoking of Function  Fn is invoked at the compile time.      1) The function is invoked at the run time.
                              (compiler parses at compile time)

2) Common Terms	:         It is known as overloading,             2) It is known as overriding, late binding, 
                          early binding, and static binding.	     and dynamic binding.                 

3) Method Name            In Overloading, more than one method    3) In Overriding, more than one method 
& Parameters              has the same name but with different       has the same name, number,
                          number or type of parameters.              and type of parameters.
	            	
4) Carriers	              It is achieved with function and        4) It is achieved with virtual functions                 operator overloading.	                  functions and pointers.
                                               

5) Execution Time	      It executes faster than run-time 	      5) It executes slower than compile-time 
                          polymorphism at the compile time.          polymorphism  at the run time.

6) Flexibility	          It is less flexible as everything 	  6) It is more flexible as everything 
                          executes at the compile time.              executes at the run time.

7)                        Overloading req single class            7) Overriding req 2 classes (inheritance)

8)                        Fn signature (fn, name, datatype, return) 
                          req for overloading
__________________________________________________________________________________________________
# Class
__________________________________________________________________________________________________
> A class is a blueprint for the object. 

Class is created to store data (variables) and methods in one place.

Normally we create variable to store data and create fn
ex. suppose we create list and pass it to a fn, then a class can store both list and fn in one place 

ex. student class has attributes (properties or variables) name, class, roll no and fns getFirstName(), setMarks()
__________________________________________________________________________________________________
# Object : 

> In Python everything is an object, which means every entity has some metadata (called attributes) and associated functionality (called methods).

> An object represents a real world entity.

+ An object is an instance of a class. 

> Objects are created dynamically, using heap memory

+ Internally, new method creates object in python (only say if asked in interview)

+ x = Class() [x is a reference variable that contains a reference to a object of class.]

+ An object can contain the references to other objects (inheritance)
__________________________________________________________________________________________________
# How is an object different from a class?
__________________________________________________________________________________________________
+ A class can be considered as a template or blueprint from which you can create objects. 
Objects are instances of a class that executes in the machine. 
+ Objects are real-world physical entities, whereas a class is a logical collection of similar objects. 
+ Developers can create as many objects as needed, but class is declared only once. 
+ Class does not occupy any memory when it is created, whereas memory is allocated as soon as an object is created. Class is useless unless its object is created.
+ Objects can be declared or created in many ways using different keywords (based on the programming language). But class can be declared and defined in one way only.
__________________________________________________________________________________________________
# Methods
Methods are functions defined inside the body of a class. They are used to define the behaviors of an object.
__________________________________________________________________________________________________
# Constructor : 
+ A special method that is called by default when object is created. It has no return type. 
+ Constructor is required to create a new instance of the class
+ Its role: to assign default value to variable when an object of the class is created
_________________________________________________________________________________________________
# Types of constructors : 
_________________________________________________________________________________________________
+ Default constructor: The default constructor is a simple constructor which doesn’t accept any arguments. Its definition has only one argument which is a reference to the instance being constructed.

+ Parameterized constructor: constructor with parameters is known as parameterized constructor. The parameterized constructor takes its first argument as a reference to the instance being constructed known as self and the rest of the arguments are provided by the programmer.
_________________________________________________________________________________________________
# The self keyword 
_________________________________________________________________________________________________
+ The self is a Python keyword that represents a variable that holds the instance of an object.
# Compulsory to write self as parameter first for every method unless static method
self allows access to the attributes and methods to each object in python. This allows each object to have its own attributes and methods. Thus, even long before creating these objects, we reference the objects as self while defining the class.
_________________________________________________________________________________________________
# Object-oriented programming lets the developers use variables at the class level or the instance level. 

+ Class Variables — Declared inside the class definition (but outside any of the instance methods). 

They are not tied to any particular object of the class, hence shared across all the objects of the class. 

Modifying a class variable affects all objects instance at the same time.

+ Instance Variable — Declared inside the constructor method of class (the __init__ method). They are tied to the particular object instance of the class, hence the contents of an instance variable are completely independent from one object instance to the other.
_________________________________________________________________________________________________
# Default value of datatypes for both : 
+ int : 0 / string : null / float : 0.0 / boolean : false
_________________________________________________________________________________________________