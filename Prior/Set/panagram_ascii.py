from string import ascii_lowercase

string1 = "the five boxing wizards jumps quickly abd xyz" 

set1 = set(ascii_lowercase)
print(set1)

set2 = set(string1.lower())
print(set2)

x = set1 - set2  # if difference is empty set it is a panagram

print(x)

if x == set([]):
    print('it is panagram')
else:
    print('it is not a panagram')

# set([]) : empty set


# {'b', 'h', 'j', 'x', 'f', 'l', 'p', 'e', 'v', 'z', 'c', 'q', 'u', 'o', 'm', 'k', 'r', 'n', 'w', 's', 'a', 'd', 'g', 't', 'y', 'i'}
# {'b', 'h', 'x', 'j', 'f', 'l', 'p', ' ', 'e', 'v', 'z', 'c', 'q', 'u', 'o', 'r', 'm', 'k', 'n', 'w', 's', 'a', 'd', 'g', 't', 'y', 'i'}
# set()
# it is panagram