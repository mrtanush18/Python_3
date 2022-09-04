str0 = "hello\tWorld"

def removeSpace(str1):
    if str1 == "":  # base case
        return ""
    if str1[0] == " " or str1[0] == "\t":
        return removeSpace(str1[1:])
    else:
        return str1[0] + removeSpace(str1[1:])

print(removeSpace(str0))

# o/p : helloWorld