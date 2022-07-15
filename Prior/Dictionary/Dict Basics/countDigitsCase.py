# Take sentence as user and check no. of digits, lowercase letters, uppercase letters, store count in  dictionary

dict = {}
digits = ['0','1','2','3','4','5','6','7','8','9']
upperCase = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lowercase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

str1 = "a fox jumps over a fox"

countDigits = 0
countLowerCase = 0
countUpperCase = 0

for i in str1:
    if i in digits:
        countDigits = countDigits + 1
    if i in upperCase:
        countUpperCase = countUpperCase + 1
    if i in lowercase:
        countLowerCase = countLowerCase + 1

print('Total uppercase: ',countUpperCase)
print('Total lowercase: ',countLowerCase)
print('Total digits: ',countDigits)

# o/p:
# Total uppercase:  0
# Total lowercase:  17
# Total digits:  0