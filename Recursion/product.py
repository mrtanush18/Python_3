
def calcProduct(m,n):
    if n == 0:
        return 0
    if n == -1:
        return -m
    if n > 0:
        return(m + calcProduct(m,n-1))
    else:
        return(-m + calcProduct(m,n+1))

print(calcProduct(2,-6))

# o/p : 12 (m=2, n=6)
# o/p : -12 (m=2, n= -6)