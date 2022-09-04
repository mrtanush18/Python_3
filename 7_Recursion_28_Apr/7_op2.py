def fn2(x):
    if x > 0:
        x -= 1
        fn2(x)
        print(x,end=" ")
        x -= 1
        fn2(x)

fn2(4)

# o/p : 0 1 2 0 3 0 1 (x=4)

# STACK TREE
# x = 1 so x = 0 fn(0)
# x = 2 so x = 1 fn(1)
# x = 3 so x = 2 fn(2)       x = 2 so x = 1 fn(1) # x = 1 so x = 0 fn(0)
# x = 4 so x - 1 = 3 fn(3)   x = 3 so x = 2 so x = 1 fn(1) so x = 1 so x = 0 fn(0)