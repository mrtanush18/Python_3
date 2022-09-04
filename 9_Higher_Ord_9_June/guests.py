# print 9 guests, 2 ppl brought guests

import functools
list1 = [
{"name": "Zeke", "vegan": True, "brought_guests": True,
"guests": [{"name": "Amanda", "vegan": False}, {"name": "Wayne", "vegan": True}]},
{"name": "Xavier", "vegan": True, "brought_guests": False},
{"name": "Yohanna", "vegan": False, "brought_guests": True, 
"guests": [{"name": "Lily", "vegan": True}, {"name": "Stefano", "vegan": True}]},
{"name": "Kael", "vegan": False, "brought_guests": False},
{"name": "Landon", "vegan": True, "brought_guests": False}]


def totalGuests(x,y):
    guests = 0
    moreGuests = 0
    list0 = []
    for i in list1:
        for k,v in i.items():
            if k=='name':
                guests = guests + 1
            temp = type(v) 
            if temp == list:
                moreGuests = moreGuests + 1
                for i in v:
                    for k,v in i.items():
                        if k == 'name':
                            guests = guests + 1
    list0.append(guests)
    list0.append(moreGuests)
    return list0 

    # print('Total guests:',guests)
    # print(moreGuests,'people brought guests')


# totalGuests(list1)

total = functools.reduce(totalGuests, list1)

print(total)