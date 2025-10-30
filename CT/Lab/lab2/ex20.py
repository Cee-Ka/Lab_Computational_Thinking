from datetime import datetime

class Account:
    def __init__(self, owner, pin, balance=0):
        self.owner, self.pin, self.balance = owner, pin, balance


class Transaction:
    def __init__(self, t_type, amount):
        self.date = datetime.now()
        self.type, self.amount = t_type, amount


class ATM:
    def __init__(self):
        self.account = None
        self.transactions = []

    def insert_card(self, account):
        self.account = account
        print(f"{account.owner}'s card inserted")

    def enter_pin(self, pin):
        if self.account and pin == self.account.pin:
            print("Correct PIN")
            return True
        print("Incorrect PIN")
        return False

    def withdraw(self, amount):
        if self.account.balance >= amount:
            self.account.balance -= amount
            self.transactions.append(Transaction("Withdraw", amount))
            print(f"Withdrawed {amount} VND. Balance: {self.account.balance} VND")
        else:
            print("Decline: Not enough money")

    def deposit(self, amount):
        self.account.balance += amount
        self.transactions.append(Transaction("Deposit", amount))
        print(f"Deposited {amount} VND. Balance: {self.account.balance} VND")

    def print_statement(self):
        print(f"\nAccount: {self.account.owner}:")
        for t in self.transactions:
            print(f"{t.date} | {t.type}: {t.amount} VND")
        print(f"Balance: {self.account.balance} VND")


acc = Account("Nguyen Van An", "1234", 5000000)
atm = ATM()

atm.insert_card(acc)
if atm.enter_pin("1234"):
    atm.withdraw(1000000)
    atm.deposit(500000)
    atm.withdraw(4000000)
    atm.print_statement()
