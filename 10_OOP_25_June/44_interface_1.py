from abc import ABC, abstractmethod

class Bank(ABC): # interface
    @abstractmethod
    def balance_chq(s):
        pass

    @abstractmethod
    def interest(s):
        pass

class SBI(Bank):
    def balance_chq(s):
        print(5000)

    def interest(s):
        print("5%")

obj1 = SBI()
obj1.balance_chq()
obj1.interest()

