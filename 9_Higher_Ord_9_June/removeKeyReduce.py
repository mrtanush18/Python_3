# KEEP REVISING

import functools

list2 = [{"email":"x@gmail.com", "name" : "x", "status" : "active"},{"email":"y@gmail.com", "name" : "y", "status" : "active"},{"email":"z@gmail.com", "name" : "z", "status" : "inactive"}]

# list3 = []
# new_dict = {}
a = {}
i = 1

def noName(x,y):
    # global new_dict
    # for k,v in x.items():
    #     if k != "name":
    #         new_dict[k] = v
    
    # list3.append(new_dict)
    # return list3
    # print(type(list3))

    # print(x)
    # print(y)
    # x[y["email"]] = y["status"]
    global a, i
    x["email"+str(i)] = y["email"] 
    x["status"+str(i)] = y["status"]
    a.update(x)
    i = i + 1
    return a

                
out = [functools.reduce(noName, list2, {})] # initializer

print(out)

# print(list(noName(list2)))

# O/P : 
# [{'email1': 'x@gmail.com', 'status1': 'active', 'email2': 'y@gmail.com', 'status2': 'active', 'email3': 'z@gmail.com', 'status3': 'inactive'}]
