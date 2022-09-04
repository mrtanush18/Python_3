# ASSIGN fn to reference variable  

def fn1(text):
    return text.upper()

print(fn1("hello"))

x = fn1  

print(x("hello"))

'''
o/p : 
HELLO
HELLO
'''

# PASS Fn to a Fn

def fn2(text):
    return text.lower()

def fn3(func):          # func to get a fn as a parameter
    msg = func("bye")  
    print(msg)

fn3(fn1)                # fn3(func)
fn3(fn2)

'''
o/p : 
BYE
bye
'''

# RETURN fn when passing value to a reference variable 

def fn4(a):
    def fn5(b):
        return a + b

    return fn5      # line part of fn4

z = fn4(15)     # assign fn4 to z

print(z(10))    # calls fn5

# o/p : 25