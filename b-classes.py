class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def make_withdrawal(self, amount,amount2, amount3):
        self.amount = amount
        self.withdrew = amount - amount2 - amount3
    def make_deposit(self, amount, amount2, amount3):
        self.deposit = amount + amount2 + amount3
# ``
    def make_withdrawal2(self, amount,amount2):
            self.amount = amount
            self.withdrew2 = amount + amount2 
    def make_deposit2(self, amount, amount2):
            self.deposit2 = amount + amount2
# 
    def make_withdrawal3(self, amount,amount2,amount3):
            self.amount = amount
            self.withdrew3 = amount + amount2 + amount3 
    def make_deposit3(self, amount):
            self.deposit3 = amount


john = User('John Doe', 15000)
john.make_withdrawal(3040,190,4230)
print(f"Hi {john.name}, you withdrew ${john.withdrew}, your new balance is ${john.balance} ")

print('*******************')
robert = User('robert fern', 1230030)
robert.make_withdrawal2(-1224,-123)
robert.make_deposit2(1224,12423)
balance2 = robert.balance - robert.withdrew2 - robert.deposit2
print(f'Hi {robert.name} u made a deposited of ${robert.deposit2} and withdrew ${robert.withdrew2} your current balance is ${balance2}')

print('*******************')
mary = User('mary alectonor', 1230030)
mary.make_withdrawal3(-1224,-123,-3435)
mary.make_deposit3(10012)
balance3 = mary.balance - mary.withdrew3 - mary.deposit3
print(f'Hi {mary.name} u made a deposited of ${mary.deposit3} and withdrew ${mary.withdrew3} your current balance is ${balance3}')
print('*******************')

transfer = 12424
john.balance -= transfer
balance3 += transfer
print(f"John u sent ${transfer} to mary, your account balance is ${john.balance} and mary's account balance is ${balance3}  ")
