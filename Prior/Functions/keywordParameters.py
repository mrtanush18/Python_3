def student(fName, lName):
    print(fName, lName)

# checks keyword when passing keyword parameters
student(fName="amit",lName="roy") 
student(lName="roy",fName="amit")

# Same fn def as above
def student1(fName, lName):
    print(fName, lName)

# checks order without passing keyword parameters
student1("ram","patil")  
student1("patil","ram")

# o/p : 
# amit roy
# amit roy 
# ram patil
# patil ram