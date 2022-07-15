list0 = ['a','b','c','d']
dict1  = {'b':10, 'e':20}
# key = 'b'

def chk(list2, dict2):
    key1 = input('Enter key: ')
    for k in dict2.keys():
        if key1 == k and k in list2:
            return dict2[k]
        else:
            return "404"

print(chk(list0,dict1))