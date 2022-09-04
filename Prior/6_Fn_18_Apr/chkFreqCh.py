string = "my bblack umbrellaa"

def chkFreqCh(str):
    dict = {}
    for i in range(len(str)):  # string to dict
        if str[i] not in dict.keys():
            dict[str[i]] = 1               
        if str[i] in dict.keys():
            dict[str[i]] = dict[str[i]] + 1
    print(dict)

    maxElement = max(dict.values()) # max method to find max element
    print(maxElement)

    for k in dict.keys():
        if dict[k] == maxElement:   # find max element in dict            
            print("Most repeated character is ",k)

chkFreqCh(string) # fn call

# o/p:
# {'m': 3, 'y': 2, ' ': 3, 'b': 4, 'l': 4, 'a': 4, 'c': 2, 'k': 2, 'u': 2, 'r': 2, 'e': 2}
# 4
# Most repeated character is  b
# Most repeated character is  l
# Most repeated character is  a