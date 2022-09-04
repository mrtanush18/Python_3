list1 = ['madam', 'mom', 'python'] 
list2=[]
new = []
def fn1(a):
    str1 = ""
    for i in a:
        str1 = i + str1
    str1 = str1.strip()
    a = a.strip()
    if a == str1: 
        list2.append(a)
    return list2
list(filter(fn1, list1))
print(list2)