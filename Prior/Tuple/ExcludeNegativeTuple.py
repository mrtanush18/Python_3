list = [(4,2,3),(-2,3,4),(-5,2,3),(4,9)]

positives = []

for tuple in list:
    count = 0
    for value in tuple:
        length = len(tuple)
        if value > 0:
            count = count + 1
    if count == length:
        positives.append(tuple)
        
print(positives)

