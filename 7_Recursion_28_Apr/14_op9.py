def fn2(a,b):
    if b == 0:
        return 1
    if b % 2 == 0:
        return fn2(a*a, b//2)
    return fn2(a*a, b//2)*a

print(fn2(4,3))

# o/p :
