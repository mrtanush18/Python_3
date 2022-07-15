# Reverse key and value
dict = {0:'red', 1:'green', 2: 'purple', 3: 'blue'}

# key = []
# value = []

new = {v : k for k,v in dict.items()}

# for k,v in dict.items():
#     new[v] = k

print(new)

# o/p : {'red': 0, 'green': 1, 'purple': 2, 'blue': 3}
