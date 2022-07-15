import math

list0 = [1,2,3,4,5]

ans = map(lambda x: math.factorial(x), list0)

print(list(ans))

# o/p : [1, 2, 6, 24, 120]
