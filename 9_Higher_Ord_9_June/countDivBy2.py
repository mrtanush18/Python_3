import functools

list0 = [22,4,12,43,19,71,20]
evenCount = 0

def chkDivBy2(x,y):
    global evenCount
    if x % 2 == 0 or y % 2 == 0:
        evenCount = evenCount + 1
    return evenCount
    
divBy2 = functools.reduce(chkDivBy2, list0)

print(divBy2)

# o/p : 4