class BankAccount:
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount


    def deposit(self):
        self.balance += self.amount
        return self.balance


    def widthdraw(self):
        if self.balance < self.amount:
            return False
        else:
            self.balance = self.balance - self.amount
            return self.balance


bc1 = BankAccount(500, 506)
#print(f"Your new balance is {bc1.deposit()} after your deposit")
if bc1.widthdraw() is False:
    print("You cannot withdraw!")
else:
    print(f"Your new balance is {bc1.widthdraw()} after your widthdraw")