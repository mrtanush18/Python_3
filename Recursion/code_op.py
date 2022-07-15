# o/p : 10 5 0 5 10

def f(n):
    if n == 0:
        print(n)
        return
    print(n)   # head recursion
    f(n-5)     
    print(n)   # tail recursion


f(10)