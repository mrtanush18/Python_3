# o/p : 3 2 1 1 2 3

def fn1(n):
    if n == 0:
        return
    else:
        print(n, end=" ")
        fn1(n-1)
        print(n, end=" ")

fn1(3)