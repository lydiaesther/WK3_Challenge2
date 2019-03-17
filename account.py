class BankAccount(object):
    def __init__(self):
        self.balance = 0

    def get_balance(self):
        if(self.balance == 'closed'):
            raise ValueError('ValueError')
        return self.balance

    def open(self):
        self.balance = 0

    def deposit(self, amount):
        if(self.balance == 'closed' or amount < 0):
            raise ValueError('ValueError')
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if(self.balance == 'closed' or amount < 0):
            raise ValueError('ValueError')
        self.balance = self.balance - amount

    def close(self):
        self.balance = "closed"

    
    def __str__(self): 
        return 'Balance on account: UGX' + str(self.balance)

   
myAccount = BankAccount() 

myAccount.deposit(500000)
myAccount.withdraw(150000)
print("Lydia's " + str(myAccount))