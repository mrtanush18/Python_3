def fn1(n):
    if n > 100:
        return n-10
    return fn1(fn1(n+11))

print(fn1(99))

# o/p : 91

# STACK TREE