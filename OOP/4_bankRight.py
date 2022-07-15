class bank:
    bankBal = 0

    def __init__(self):     # OR def setAccount(self):
        self.accNo = int(input('Enter acc no '))
        self.name = input('Enter name ')
        self.bal = int(input('Enter current balance '))
        bank.bankBal = bank.bankBal + self.bal

    def showAccount(s):
        print(s.accNo)
        print(s.name)
        print(s.bal)

    @staticmethod
    def totalBal():
        # total = bank.bankBal
        print('Total: ',bank.bankBal)

list0 = []

while(1):
    ans = input('Add customer?')
    if ans == 'yes':
        n = int(input('How many?'))
        for i in range(n):
            temp = "cust" + str(i)
            list0.append(temp)
            list0[i] = bank()
            list0[i].showAccount()
            list0[i].totalBal()
    else:
        break








# cust1 = bank()
# cust2 = bank()

# cust1.setAccount()
# cust1.showAccount()
# cust1.totalBal()
# cust2.setAccount()
# cust2.showAccount()
# cust2.totalBal()

