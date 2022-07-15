def fn3(a,n):
    if n == 1:
        return a[0]
    else:
        x = fn3(a,n-1)
    if(x > a[n-1]):
        return x
    else:
        return a[n-1]

list1 = [12,10,30,50,100]

print(fn3(list1,5))

# o/p : 

# STACK TREE:
