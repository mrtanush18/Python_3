def fn1(n):
    i = 0
    if(n > 1):
        fn1(n-1)      # stack frame t to b : 5 > 4 > 3 > 2 > 1
    for i in range(n): # runs once above condition fails 
        print(" * ")
    print("\n")

fn1(5)

# o/p:
#  *   n = 1, range starts from 0


#  *   n = 2
#  *

 
#  *   n = 3
#  *
#  *


#  *   n = 4
#  *
#  *
#  *


#  *   n = 5
#  *
#  *
#  *
#  *


