dict = {1:'python', 2:'Java', 3:'C++', 4:'Java', 5:'python'}
new_dict = {}

for key, value in dict.items():
    if value not in new_dict.values():
        new_dict[key] = value

for key, value in dict.items():
    if key == 4:
        dict[key] = "php"
    if key == 5:
        dict[key] = "ruby"

print(dict)

dict.pop(4)
dict.pop(5)

print(dict)

# o/p:
# {1: 'python', 2: 'Java', 3: 'C++', 4: 'php', 5: 'ruby'}
# {1: 'python', 2: 'Java', 3: 'C++'}