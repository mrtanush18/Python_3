# Print dict items with key div by 3

dict1 = {45:"Ram", 78:"Sam", 22:"Ashok"}

def divBy3(k):      # k is a list
    div3 = {}
    for item in k:
        if item % 3 == 0:
            div3[item] = dict1[item]    # key = value

    print(div3)

divBy3(dict1.keys()) # .keys() gives a list of keys >> dict_keys([45, 78, 22]) 

# o/p : {45: 'Ram', 78: 'Sam'}



# print(filter(divBy3, dict1.keys())) # error

# divBy3 = {i:dict1[i] for i in dict1 if i%3==0} # comprehension