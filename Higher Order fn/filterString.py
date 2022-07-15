list0 = ['A', 'B', 'D', 1, 2, 3]


def ifChar(x):
    if type(x) == str:
        return x

out = filter(ifChar, list0)

print(list(out))

# o/p : ['A', 'B', 'D']

# OR

# list0 = ['A', 'B', 'D', '1', '2', '3']

# out = filter(str.isalpha, list0)

# print(list(out))

# o/p : ['A', 'B', 'D']