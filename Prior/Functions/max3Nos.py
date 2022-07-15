x = int(input())
y = int(input())
z = int(input())

def MaxNumber(a,b,c):
    if(a>b):
        if(a>c):
            return a
    if(b>c):
            return b
    else:
        return c

max = MaxNumber(x,y,z)

print(max)