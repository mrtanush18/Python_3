# name, cust_id, bal, total bal
# WRONG WAY :
class bank:
    def __init__(self):
        self.name = ""
        self.cust_id = ""
        self.bal = 0

    def addCustomer(c):
        ans = input('Add more customer data?')
        if(ans == 'yes'):
            n = int(input('How many?'))
            for i in range(0,n):
                    temp = "cust" + str(i+1)
                    list0.append(temp)
                    print(list0[i])
                    list0[i] = bank()
                    list0[i].setDetails(list0)
                    list0[i].showDetails(list0)
        

    def setDetails(s,list0):
        for obj in list0:
            obj.name = input('Enter name: ')
            obj.cust_id = input('Enter ID: ')
            obj.bal = int(input('Enter current balance: '))
        s.addCustomer()

    def showDetails(s,list0):
        total = 0
        print("You entered:")
        for obj in list0:
            print(obj.name)
            print(obj.cust_id)
            print(obj.bal)

        total = total + obj.bal
        print('Total bank balance: ',total)

list0 = []

cust1 = bank()

cust1.setDetails(list0)

list0.append(cust1)

cust1.showDetails(list0)
