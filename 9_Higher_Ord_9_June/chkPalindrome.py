list0 = ['1234321','programming','madam']

def chkPalindrome(x):
    temp = x
    if x[::-1] == temp:
        return x

palindrome = filter(chkPalindrome, list0)

print(list(palindrome))

# o/p : ['1234321', 'madam']