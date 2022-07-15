str1 = "programming is best for all"
dict1 = {"all":"student"}

for k,v in dict1.items():
    str1 = str1.replace(k,v)
    
print(str1)