class person:
    def __init__(self):
        self.name = input('Enter your name: ')
        self.age = int(input('Enter your age: '))
        self.pin = int(input('Enter your pincode: '))

    def showDetails(s):
        print(s.name)
        print(s.age)
        print(s.pin)


list0 = []

while(1):
    ans = input('Add person data? ')
    if(ans == 'yes'):
        n = int(input('How many people? '))
        for i in range(n):
            temp = "obj" + str(i)
            list0.append(temp)
            list0[i] = person()

    else:
        break

    ageList = []

    for x in list0:
        ageList.append(x.age)

    ageList.sort()

    for y in list0:
        if ageList[-1] == y.age:
            print('Most elder person is',y.name)

