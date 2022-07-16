# What is a namespace?
A namespace in Python ensures that object names in a program are unique and can be used without any conflict.

Objects in python, be it fn or variable have a name & req space. ex a, fn fn1()
real life. 4 to 5 devs are working on various parts of a project. Suppose all code is integrated & some classes created by devs have same name. At runtime which class's object will be created? 
Each dev will create a namespace which will have their class. Then object will be created after checking namespace, this will avoid confusion of class having same name.

# Types of namespace : local, global, built in store local, global variables & variables related to built in fns
Variables having same name in local or global namespace can be easily differentiated by which namespace they are in

IDLE : write a single line of code, which gets interpreted
in a file, program written is compiled

In python code first gets compiled then interpreted

# What is scope?
Local variables can be accessed only within a function where they were created

# Can fns, variables be considered as object ?
Everything in python is a object

# How does memory management happen in Python ?
Stack and heap
In recursion, functions req stack memory to create stack frames
Error in recursion is called stack overflow

Heap memory is used for creating objects

# What is compile and run time ?
ex. suppose we have to create array
Checking of array name, datatype, declaration happens at compile time or compiler gives error so bytes of space in main memory is reserved for array at compile time and happens in stack

Then if we have dynamic array. ex. if we req user i/p for size of multidimensional array then heap memory is allocated for this at run time

# What is garbage colector ?
It is a background process written by python team to check no. of variables, objects and check if they are in use (their reference is there) by a running process and if not remove them from main memory. ex. if in a application, login is going on then only login module should run then product module is not currently in use so garbage collector removes them from main memory.

Program when loaded into main memory is called a process

# Daemon thread (used in multithreading): Garabage collector
The threads which are always going to run in the background that provides supports to main or non-daemon threads, those background executing threads are considered as Daemon Threads. The Daemon Thread does not block the main thread from exiting and continues to run in the background. This article is based on threading in python, here we discuss daemon thread with examples.

There is one of the best examples of a daemon thread is Garbage Collector because we assume that the main thread is executing or running, at that time any memory problem occurs then immediately python virtual machine(PVM) is going to execute Garbage Collector. The Garbage Collector is going to execute in the background and destroy all the useless objects and then free memory by default will be provided, once there is free memory will available then the main thread is going to be executed without any problem.

# What is continue keyword ?

# What is a keyword, identifiers ?
> Identifiers are names of fns or variables or class or object given by the user
> Keywords are built in fns of a language, they are included in the language
ex. for, while, break, continue are keywords & can't be used by user.

# What is just in time (JIT) compiler ?
Java code is compiled and we get bytecode (.class) which can be run in any machine having JVM (internally it uses JIT compiler) 

Python also has Python Virtual machine which internally uses JIT compiler

C++ code can't be run in any machine

# cmd line is a ex of interpreter where it gives o/p or error after writing a single line of cmd

# pep 8 : python documentation which has tips for better and newer ways of writing code. 
ex writing a class or fn or variable in a better way to increase performance

<!-- Nxt test after 1, 1 1/2 month after obj oriented, exception handling, regular expressions -->

