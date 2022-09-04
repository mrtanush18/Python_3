# panagram or not, each alphabet should be there in string
string1 = "the five boxing wizards jumps quickly abd xyz" 
set1 = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}

flag = 0

for i in range(len(string1)):
    if string1[i] in set1:
        flag = flag + 1
    else:
        flag = flag - 1

if flag >= 26:
    print('present',flag)
else:
    print('false',flag)
