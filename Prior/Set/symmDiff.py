set1 = {10,20,30}
set2 = {20,40,50}

uniqueToSet1 = set1.difference(set2)
print(uniqueToSet1)

uniqueToBoth = set1.symmetric_difference(set2) 
print(uniqueToBoth)  

common = set1.intersection(set2)
print(common)

# {10, 30}  # Return a set that contains the items that only exist in set x, and not in set y:
# {40, 10, 50, 30} # merge both sets so that same in both, 20 not included
# {20}  # common in both