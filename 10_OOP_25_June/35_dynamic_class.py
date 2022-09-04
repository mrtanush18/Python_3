class country:
    def __init__(self, country):
        self.xcountry = country

    def language(s,lang):
        s.language = lang

    def output(o):
        print(o.xcountry)
        print(o.language)
        print("")


list0 = []

while(1):
    ans = input('Add country? ')
    if ans == 'yes':
        n = int(input('How many? '))
        for i in range(n):
            temp = "obj" + str(i)
            list0.append(temp)
            list0[i] = country(input('Which country? '))
            list0[i].language(input('Language? '))
    else:
        print("\nData:")
        for i in range(n):
            list0[i].output()
        break

# STATIC CODE:
# obj1 = india()
# list0.append(obj1)
# obj2 = uk()
# list0.append(obj2)
# obj3 = france()
# list0.append(obj3)

# for i in range(3):
#     list0[i].language()