def squareNos(x,y):
    sq1 = x*x
    sq2 = y*y
    def addSquares(sq1,sq2):
        sum = sq1 + sq2
        return sum
    res = addSquares(sq1,sq2)
    print(res)
    return res,sq1,sq2
        
result,a,b = squareNos(2,3)
# result = squareNos(2,3) # o/p is tuple
print(result,a,b)

# o/p:
# 13
# 13 4 9