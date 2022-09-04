import functools
# vegan = 6 , not vegan = 3
list1 = [
{"name": "Zeke", "vegan": True, "brought_guests": True,
"guests": [{"name": "Amanda", "vegan": False}, {"name": "Wayne", "vegan": True}]},
{"name": "Xavier", "vegan": True, "brought_guests": False},
{"name": "Yohanna", "vegan": False, "brought_guests": True, 
"guests": [{"name": "Lily", "vegan": True}, {"name": "Stefano", "vegan": True}]},
{"name": "Kael", "vegan": False, "brought_guests": False},
{"name": "Landon", "vegan": True, "brought_guests": False}]

def totalGuests(x,y):
    vegan = 0
    notVegan = 0
    list0 = []
    for i in list1:
        for k,v in i.items():
            if v==True and k=="vegan":
                vegan = vegan + 1
            if v==False and k=="vegan":
                notVegan = notVegan + 1
            temp = type(v) 
            if temp == list:
                for i in v:
                    for k,v in i.items():
                        if v==True and k=="vegan":
                            vegan = vegan + 1
                        if v==False and k=="vegan":
                            notVegan = notVegan + 1
    list0.append(vegan)
    list0.append(notVegan)
    return list0 

# print(totalGuests(list1))

total = functools.reduce(totalGuests, list1)

print(total)

# o/p : [6, 3]