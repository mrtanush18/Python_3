class onlyEven(list):
    
    list1 = []
    def chkTypeValue(s,n):
        if not isinstance(n,int):
            raise TypeError('Value of i must be integer not string')
        
        if n % 2: # 0 : false
            raise ValueError('Only even nos are allowed')
        onlyEven.list1.append(n)
        print(onlyEven.list1)

     
obj1 = onlyEven()
obj1.chkTypeValue(2)
obj1.chkTypeValue(4)
obj1.chkTypeValue(3)  # St1
obj1.chkTypeValue('a') # St2

# Swap st1 & st2 to see exceptions in o/p