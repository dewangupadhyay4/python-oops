class BankAccount:
    def __init__(self,owner,balance):
        self.owner=owner
        self.__balance=balance

    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount

    def withdraw(self,amount):
        if 0<amount<=self.__balance:
            self.__balance-=amount
        else:
            print("Insufficient Balance")

    def get_balance(self):
        return self.__balance
    
acc=BankAccount("Dewang", 150000)
print("owner name: ",acc.owner)
print("Balance ",acc.get_balance())

acc.deposit(50000)
acc.withdraw(10000)
print("Updated balance is: ",acc.get_balance())