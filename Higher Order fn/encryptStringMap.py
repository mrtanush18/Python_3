str1 = "this is a python project"

def encrypt(x):
    for i in x:
        value = ord(x)      # converts to ascii value
        value = value + 1
    return chr(value)       # chr returns original character 

cipher = map(encrypt, str1)

print(''.join(cipher))      # join concats each ch to single string

# o/p : uijt!jt!b!qzuipo!qspkfdu    # (spaces = !)