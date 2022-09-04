# reverse string using recursion

str = "hello"

def str_reverse(s):
    if s == "":   # terminating condition
        return s
    else:
        return str_reverse(s[1:]) + s[0] # passing only s[1:] to slice string excluding 1st ch
                                        
print(str_reverse(str))

# o/p : olleh