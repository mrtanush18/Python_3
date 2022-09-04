str1 = "mountain"
vowels = ["a","e","i","o","u"]
count1 = 0

def countVowel(str2,index):
    global count1
    if index == len(str2):
        return
    if str2[index] in vowels:
        count1 = count1 + 1
    countVowel(str2, index + 1) 

countVowel(str1,0)

print(count1)

# o/p : 4