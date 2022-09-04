tuple = (4,1,4,1,2,3)
list = []

for v in tuple:
    if v not in list:
        list.append(v)
if len(tuple) != len(list):
    print("not unique")
else:
    print("unique")


