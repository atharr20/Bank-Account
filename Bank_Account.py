class BankAccount:
    total_deposits=0
    total_withdraws=0

    def __init__(self, int_rate, balance):
        self.int_rate=int_rate
        self.balance=balance

    def deposit(self, amount):
        self.amount=amount
        return {self.amount}

    def withdraw(self, amount):
        if self.amount < amount:
            print("Insufficient funds.")
            return {self.balance}-5
        self.amount-=amount
        return self

    def display_account_info(self):
        return(f"Balance: {self.balance}")
        
    def yield_interest(self):
        return {self.balance}*(1.075)


BA1=BankAccount(.07,500)
BA2=BankAccount(.07,5000)

print(BA1)
            
# BA1.deposit(2).deposit(2).deposit(2).withdraw(12.5).yield_interest().display_account_info()

# BA2.deposit(752.8).deposit(752.8).withdraw(100).withdraw(100).withdraw(100).withdraw(100).yield_interest().display_account_info()