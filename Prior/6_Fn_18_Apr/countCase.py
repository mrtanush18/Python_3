# On passing string to fn, return no. of uppercase & lowercase together

string = input()

def countCase(inString):
    upperCount = 0
    lowerCount = 0
    for i in range(len(inString)):
        if ord(inString[i]) in range(65,91): # ord returns ascii value (A-Z is 65 to 90)
            upperCount = upperCount + 1
        if ord(inString[i]) in range(97,123):  # (a-z is 97 to 122)
            lowerCount = lowerCount + 1
        if ord(inString[i]) in range(32,65):  # (nos, special ch is 32-64)
            print("Invalid input")
            break
    if upperCount > 0 or lowerCount > 0:
        print('There are ',upperCount,' uppercase characters and ', lowerCount, ' lowercase characters')

countCase(string)

# o/p : aBc ddd eee FFF
# There are  4  uppercase characters and  8  lowercase characters

# OR
# 123$
# Invalid input