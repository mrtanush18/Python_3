# >> Create dict with key as square and value as double of nos in range 0 to 5
# using for loop
new_dict = {}

for value in range(0,5):
    key = value**2  # square
    new_value = value*2 # double
    new_dict[key] = new_value

print(new_dict)

# > Using comprehension
new_dict_compre = {value**2 : value*2 for value in range(0,5)}
print(new_dict_compre)