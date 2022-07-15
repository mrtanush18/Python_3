limit = 1000

def fn1(n):
    if n <= 0:
        return
    if n > limit:
        return
    print(n,end=" ")
    fn1(2*n)
    print(n,end=" ")

fn1(100)

# STACK TREE : 

