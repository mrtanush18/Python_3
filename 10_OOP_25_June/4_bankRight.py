class bank:
    bankBal = 0

    def __init__(self):     # OR def setAccount(self):
        print("")
        self.accNo = int(input('Enter acc no '))
        self.name = input('Enter name ')
        self.bal = int(input('Enter current balance '))
        bank.bankBal = bank.bankBal + self.bal

    def showAccount(s):
        print("")
        print(s.accNo)
        print(s.name)
        print(s.bal)

    @staticmethod
    def totalBal():
        # total = bank.bankBal
        print('Total: ',bank.bankBal)

list0 = []

while(1):
    ans = input('Add customer? ')
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

'''
o/p:
Add customer?yes
How many?2

Enter acc no 234
Enter name ram
Enter current balance 5000

234
ram
5000
Total:  5000

Enter acc no 456
Enter name sam
Enter current balance 6000

456
sam
6000
Total:  11000

Add customer?no
'''









