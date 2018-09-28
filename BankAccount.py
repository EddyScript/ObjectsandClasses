first_name = input("Enter first name to create account: ")
middle_name = input("Enter middle name: ")
last_name = input("Enter last name: ")

while True: 
    enter_start_balance = int(input("please deposit at least $100 to open account: "))
    if enter_start_balance <= 99:
        print("Sorry not enough to open account")
    elif enter_start_balance >= 99:
        break

balance = enter_start_balance
enter_pin = int(input("Please choose a four digit pin code: "))
PIN = enter_pin

menu = int(input("What would you like to do?: 1. Deposit 2. Withdraw 3. Change PIN : "))

if menu == 1:
    user_deposit = int(input("How much: "))
    amount = user_deposit
elif menu == 2:
    user_withdraw = int(input("How much?: "))
    withdrew = user_withdraw
elif menu == 3:
    change_pin = str(input("Whats your new PIN?: "))
    new_pin = change_pin

class BankAccount:
    def __init__(self):
        self.firstname = ""
    def UserNames(self):
        self.firstname = first_name
        self.middlename = middle_name
        self.lastname = last_name
        self.balance = balance
        self.withdraw = withdrew
        self.deposit = amount
        self.PIN = PIN
    def Deposit(self):
       self.newbalance_deposit = (balance+amount)
    def Withdraw(self):
        self.newbalance_withdraw = (balance-withdrew)
    def ChangePIN(self):
        self.PIN = new_pin
