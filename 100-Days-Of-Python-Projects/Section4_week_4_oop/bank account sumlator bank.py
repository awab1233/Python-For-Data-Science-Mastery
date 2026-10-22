# class car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
  
#     def display_info(self):
#         print(f"car brand is {self.brand}, car model is {self.model}")

# # create an object
# my_car = car("nissan", "maxima") 
# my_car.display_info()

# # create another object
# ymodel = input("enter your car model: ")
# ybrand = input("enter your car brand: ")
# your_car = car(ybrand, ymodel)
# your_car.display_info()


# BANK ACCOUNT SUMULATOR 
class BankAcount:

    # function to account details
    def __init__(self, account, balance=0):
        self.account_holder = account
        self.balance = balance

    # function to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"you have deposited {amount}. your new balance is {self.balance}")
        else:
            print("deposit amount must be greater than 0")

    # function to withdraw money
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"withdraw {amount}. your new balance is {self.balance}")
        else:
            print("withdraw amount must be greater than 0 and less than or equal to your balance")

    # function to show details
    def show_details(self):
        print("-------account details-------")
        print(f"account number: {self.account_holder}")
        print(f"account balance: {self.balance}")


# main program
accounts = {}
def great_account():
    name = input("enter your name: ").strip()
    initial_deposit = float(input("enter initial deposit amount: "))
    account = BankAcount(name, initial_deposit)
    accounts[name] = account
    print("account created successfully!")

#
def access_account():
    name = input("enter your name: ").strip()
    if name in accounts:
        account = accounts[name]
        while True:
            print("\n1. Deposit" \
                "\n2. Withdraw\n" \
                "3. Show Details\n" \
                "4. Exit")
            choice = input("choose an option (FROM 1 TO 4): ").strip()
            if choice == '1':
                amount = float(input("enter deposit amount: "))
                account.deposit(amount)
            elif choice == '2':
                amount = float(input("enter withdraw amount: "))
                account.withdraw(amount)
            elif choice == '3':
                account.show_details()
            elif choice == '4':
                print("exiting account...")
                break
            else:
                print("invalid option. please try again.")
    else:
        print("account not found. please create an account first.")
# main menu
def main_menu():
    while True:
        print("\n1. Create Account\n"\
            "2. Access Account\n"
            "3. Exit")
        choice = input("choose an option (FROM 1 TO 3): ").strip()
        if choice == '1':
            great_account()
        elif choice == '2':
            access_account()
        elif choice == '3':
            print("exiting program...")
            break
        else:
            print("invalid option. please try again.")
    
main_menu()