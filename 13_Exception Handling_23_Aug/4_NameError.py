str1 = "python"

try:
    print(str2)
except NameError:
    print('str1 is name of variable')

# o/p: str1 is name of variable

# >> og error :
# NameError: name 'str2' is not defined. Did you mean: 'str1'?