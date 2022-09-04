# Remove the items that exist in both sets:

set1 = {10,20,30,40}
set2= {30,40,50,60,70}

set1.symmetric_difference_update(set2)

print(set1)

# {70, 10, 50, 20, 60}