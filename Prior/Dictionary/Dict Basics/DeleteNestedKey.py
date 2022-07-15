mobiles = {1:{'company':"iphone", 'model': 'XR' , 'OS' : 'iOS' , 'price' : 50000}, 2:{'company':'Samsung', 'model': 'Nord10', 'OS': 'Android', 'price' : 40000}}


mobiles[3] = {'company':"vivo" , 'OS' : 'ubuntu' , 'price' : 50000}

# Delete outer key
# del(mobiles[2]) 

# Delete inner key
del(mobiles[1]['model'])

print(mobiles)

#o/p :
# {1: {'company': 'iphone', 'OS': 'iOS', 'price': 50000}, 2: {'company': 'Samsung', 'model': 'Nord10', 'OS': 'Android', 'price': 40000}, 3: {'company': 'vivo', 'OS': 'ubuntu', 'price': 50000}}