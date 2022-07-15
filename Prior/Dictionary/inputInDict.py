# Take i/p from user, create dictionary and print it

dict = {}
size = int(input("\nEnter number of keys: "))

for i in range(size):
    key , value = input("\nEnter key and value: ").split()  # one line i/p
    dict[key] = value

print('\n',dict)

dict["6"] = "ruby"
dict.update({"6":".NET"})
print('\n',dict)

# o/p: # o/p :
# {'name': 'tanush', 'age': '22'}
# {'name': 'tanush', 'age': '22', '6': '.NET'}
