# Count number of words in sentence

count = 1       # set to 1 as counting spaces bw words

string = input('Enter a sentence: ')

if string == '':
    print("Empty string")

else:
    for i in string:
        if i == ' ':
            count = count + 1

    print(count)
 
# o/p:
# Enter a sentence: a fox jumps over a fox
# 6