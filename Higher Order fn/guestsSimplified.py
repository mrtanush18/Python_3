list1 = [
{"name": "Zeke", "vegan": True, "brought_guests": True,
"guests": [{"name": "Amanda", "vegan": False}, {"name": "Wayne", "vegan": True}]}]
guests = 0
moreGuests = 0

for i in list1:
    for k,v in i.items():
        if k=='name':
            guests = guests + 1
        temp = type(v) 
        if temp == list:
            for i in v:
                for k,v in i.items():
                    if k == 'name':
                        moreGuests = moreGuests + 1

        

print(guests)
print(moreGuests)