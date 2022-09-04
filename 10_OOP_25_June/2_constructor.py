class student:
    counter = 0       # class variable
    
    # parameterised constructor
    def __init__(self,name,age):        
        self.myName = name    # myName instance variable, not name !! 
        self.myAge = age                # name, age are parameters
        self.roll_no = 0                # can change for each obect

        student.counter = student.counter + 1 

    # method to print only
    def getRollNo(x):                   # self written as x to access instance variable 
        print(x.myName)
        print(x.myAge)
        print(x.roll_no)

    def setRollNo(y,roll_no):          
        y.roll_no = roll_no

# create objects and sending data
student_1 = student("sam",18)
student_2 = student("tom",20)
student_3 = student("jerry",22)
student_4 = student("harry",35)

# call method using objects
student_1.setRollNo(49)
student_1.getRollNo()

student_2.setRollNo(50)
student_2.getRollNo()

student_3.setRollNo(51)
student_3.getRollNo()

student_4.setRollNo(54)
student_4.getRollNo()

print("Total objects created:", student.counter) # access class variable

student_1.counter = 5   # accessing & modifying class variable only for student 1

print(student_1.counter)
print(student_2.counter)

'''
o/p:
sam
18
49

tom
20
50

jerry
22
51

harry
35
54

Total objects created: 4
5
4
'''