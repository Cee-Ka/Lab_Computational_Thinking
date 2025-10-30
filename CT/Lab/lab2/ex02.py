class BankAccount:
    def __init__(self, account_number, owner, balance):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return f"deposited {amount}"
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return f"withdrawed {amount}"
        else:
            return "your balance is not enough"
    def get_balance(self):
        return self.balance
    def get_info(self):
        return f"{self.account_number} {self.owner} {self.balance}"
bank = BankAccount(1234, "Khanh", 200000)
print(bank.deposit(100000))
print(bank.withdraw(50000))
print("balance: ", bank.get_balance())