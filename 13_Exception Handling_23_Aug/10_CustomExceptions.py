class LowBalanceError(Exception):
    print('in lbe class')
    def __init__(self,cust_details):
        self.cust_details = cust_details
        print(type(cust_details))
        print(cust_details)
    def showDetails(s):
        print('in showDetails()')
        for k,v in s.cust_details.items():
            print('in for')
            print(k,':',v)

class Bank:
    def __init__(self):
        self.cust_details = {}
        self.curr_bal = 0

    def getCustDetails(s):
        print('ok')
        for i in range(1):
            ac_no = input('Enter account_no') #pk
            outer_value = {}
            for j in range(1):
                outer_value['Name'] = input()
                outer_value['Current_Bal'] = s.curr_bal
                s.cust_details[ac_no] = outer_value
              
        print(s.cust_details)

    def deposit(s):
        print(s.curr_bal)
        dep = int(input('Enter amt to deposit '))
        s.curr_bal = s.curr_bal + dep
        print(s.curr_bal)

    def withdraw(s):
        wth = int(input('Enter amt to withdraw '))   #dict
        if(wth < s.curr_bal):
            s.curr_bal = s.curr_bal - wth
        else:
            raise LowBalanceError(s.cust_details)

    def callBank(s):
        while(1):
            ans = input('Deposit?? ')
            if(ans == 'yes'):
                s.deposit()
            else:
                ans2 = input('Withdraw?? ')
                if(ans2 == 'wth'):
                    s.withdraw()
                else:
                    ans3 = input('Done?? ')
                    if(ans3 == 'yess'):
                        s.getCustDetails()
            break
        

obj1 = Bank()
obj1.callBank()
try:
    obj1.withdraw()
except LowBalanceError as obj2:
    obj2.showDetails()
    


