def fn2(i):
    if i % 2 == 1:
        i += 1
        return(i-1)
    else:
        return fn2(fn2(i-1))

print(fn2(200))