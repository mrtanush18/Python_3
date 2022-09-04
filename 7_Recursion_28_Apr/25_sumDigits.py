num = 1236

def sumDigits(n):
    sum = 0
    if n == 0:
        return 0
    else:
        r = n%10
        q = n//10
        return r + sumDigits(q)
    
print(sumDigits(num))

# o/p : 12 