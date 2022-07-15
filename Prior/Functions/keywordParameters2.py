# Used when no. of parameters is not known use *arg and **kwarg when keyword is used

def student(**kwarg): # pass any no. of keyword arguments with double *
    for key,value in kwarg.items(): # .items() like dictionary to iterate kwarg
        print(key,":",value)

# checks keyword order
student(fName="amit",lName="roy",dob="04-09-98")
student(lName="roy",fName="amit",marks="56")

def student1(*arg): # pass any no. of arguments with single *
    for value in arg: # iterate arg
        print(value)

# checks order
student1("ram","patil",60)  
student1("patil","ram",70)

# fName : amit
# lName : roy
# dob : 04-09-98
# lName : roy
# fName : amit
# marks : 56
# ram
# patil
# 60
# patil
# ram
# 70