tuple1 = ()
tuple2 = ()
tuple3 = ()
sum = 0

size1 = int(input('Enter size of tuple 1: '))

print('Enter items in tuple 1')
for i in range(size1):
    item = int(input())
    tuple1 = tuple1 + (item,)

size2 = int(input('Enter size of tuple 2: '))

print('Enter items in tuple 2')
for i in range(size2):
    item = int(input())
    tuple2 = tuple2 + (item,)

print(tuple1)
print(tuple2)

for i in range(len(tuple1)):  
    sum = tuple1[i] + tuple2[i]
    tuple3 = tuple3 + (sum,)
    
if(len(tuple2) > len(tuple1)):
    for i in range(len(tuple1),len(tuple2)):  
        sum = 0
        sum = sum + tuple2[i]
        tuple3 = tuple3 + (sum,)
        

print(tuple3)


