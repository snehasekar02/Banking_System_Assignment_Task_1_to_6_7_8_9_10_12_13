"""
1. Overload the deposit and withdraw methods in Account class as mentioned below.

deposit(amount: float): Deposit the specified amount into the account.

withdraw(amount: float): Withdraw the specified amount from the account. withdraw amount only if there is sufficient fund else display insufficient balance.

deposit(amount: int): Deposit the specified amount into the account.

withdraw(amount: int): Withdraw the specified amount from the account. withdraw amount only if there is sufficient fund else display insufficient balance.

deposit(amount: double): Deposit the specified amount into the account.

withdraw(amount: double): Withdraw the specified amount from the account. withdraw amount only if there is sufficient fund else display insufficient balance.
"""


class Account:
    def __init__(self, account_number, account_type, account_balance):
        self.__accountNumber = account_number
        self.__accountType = account_type
        self.__accountBalance = account_balance

    def getAccountNumber(self):
        return self.__accountNumber

    def setAccountNumber(self, account_number):
        self.__accountNumber = account_number

    def getAccountType(self):
        return self.__accountType

    def setAccountType(self, account_type):
        self.__accountType = account_type

    def getAccountBalance(self):
        return self.__accountBalance

    def setAccountBalance(self, account_balance):
        self.__accountBalance = account_balance

    def displayAccountInfo(self):
        print("Account Number:", self.__accountNumber)
        print("Account Type:", self.__accountType)
        print("Account Balance:", self.__accountBalance)

    def deposit(self, amount):
        if isinstance(amount, (int, float)):
            self.__accountBalance += amount
            print(f"Rs.{amount} deposited successfully")
            print(f"The New Balance is {self.__accountBalance}")
        else:
            print("Failed to deposit amount.")

    def withdraw(self, amount):
        if isinstance(amount, (int, float)):
            if amount <= self.__accountBalance:
                self.__accountBalance -= amount
                print(f"Rs.{amount} withdrawn successfully")
                print(f"The New Balance is {self.__accountBalance}")
            else:
                print("Insufficient balance.")
        else:
            print("Invalid type for withdrawal amount.")

    def calculate_interest(self) -> float:
        interest_rate = 4.50
        interest_amount = (self.__accountBalance * interest_rate) / 100
        return interest_amount


'''account = Account("89672314671", "Savings", 6000.0)
account.deposit(500)
account.withdraw(200)
account.deposit(250.50)
account.withdraw(500.50)'''

"""
2. Create Subclasses for Specific Account Types

Create subclasses for specific account types (e.g., `SavingsAccount`, `CurrentAccount`) that inherit from 
the `Account` class.
o SavingsAccount: A savings account that includes an additional attribute for interest rate. override 
the calculate_interest() from Account class method to calculate interest based on the balance and interest rate.
o CurrentAccount: A current account that includes an additional attribute overdraftLimit. A current account with 
no interest. Implement the withdraw() method to allow overdraft up to a certain limit 
(configure a constant for the overdraft limit).
"""


class SavingsAccount(Account):
    interestRate = 5.50

    def calculate_interest(self):
        interest_amount = (self.getAccountBalance() * self.interestRate) / 100
        self.setAccountBalance(self.getAccountBalance() + interest_amount)
        print(f"Interest Amount is {interest_amount}")
        print(f"The New Balance with interest is {self.getAccountBalance()}")


class CurrentAccount(Account):
    overdraft_limit = 1500.0

    def withdraw(self, amount):
        available_balance = self.getAccountBalance() + self.overdraft_limit
        if amount <= available_balance:
            self.setAccountBalance(available_balance - amount)
            print(f"Rs.{amount} withdrawn successfully")
            print(f"The New Balance is {self.getAccountBalance()}")
        else:
            print("Withdrawal amount exceeds available balance and overdraft limit.")


'''savings_account = SavingsAccount("67845901234", "Savings", 2000.0)
savings_account.calculate_interest()

current_account = CurrentAccount("78901256125", "Current", 2000.0)
current_account.withdraw(3500)'''

"""
3. Create a Bank class to represent the banking system. Perform the following operation in main method:

Display menu for user to create object for account class by calling parameter constructor. Menu should display options 
`SavingsAccount` and `CurrentAccount`. user can choose any one option to create account. 
use switch case for implementation.

deposit(amount: float): Deposit the specified amount into the account.

withdraw(amount: float): Withdraw the specified amount from the account. For saving account withdraw amount 
only if there is sufficient fund else display insufficient balance.
For Current Account withdraw limit can exceed the available balance and should not exceed the overdraft limit.

• calculate_interest(): Calculate and add interest to the account balance for savings accounts.
"""


class Bank:
    def __init__(self):
        self.accounts = []

    def create_account(self, account_number, account_type, account_balance):
        if account_type == "SavingsAccount":
            account = SavingsAccount(account_number, "Savings", account_balance)
        elif account_type == "CurrentAccount":
            account = CurrentAccount(account_number, "Current", account_balance)
        else:
            print("Invalid account type.")
            return
        self.accounts.append(account)
        print(f"{account_type} created successfully.")

    def deposit(self, account_number, amount):
        for account in self.accounts:
            if account.getAccountNumber() == account_number:
                account.deposit(amount)
                return
        print("Account not found.")

    def withdraw(self, account_number, amount):
        for account in self.accounts:
            if account.getAccountNumber() == account_number:
                account_type = account.getAccountType()
                if account_type == "Savings":
                    account.withdraw(amount)
                elif account_type == "Current":
                    account.withdraw(amount)
                return
        print("Account not found.")

    def calculate_interest(self, account_number):
        for account in self.accounts:
            if account.getAccountNumber() == account_number:
                if isinstance(account, SavingsAccount):
                    account.calculate_interest()
                    return
        print("Account not found.")


def main():
    bank = Bank()

    while True:
        print("------------------------------------------")
        print("Welcome to the banking system.")
        print("1. Create Savings Account")
        print("2. Create Current Account")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Calculate Interest for Savings Account")
        print("6. Quit")
        print("------------------------------------------")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            account_number = input("Enter account number: ")
            account_balance = float(input("Enter initial balance: "))
            bank.create_account(account_number, "SavingsAccount", account_balance)
        elif choice == 2:
            account_number = input("Enter account number: ")
            account_balance = float(input("Enter initial balance: "))
            bank.create_account(account_number, "CurrentAccount", account_balance)
        elif choice == 3:
            account_number = input("Enter account number: ")
            amount = float(input("Enter deposit amount: "))
            bank.deposit(account_number, amount)
        elif choice == 4:
            account_number = input("Enter account number: ")
            amount = float(input("Enter withdrawal amount: "))
            bank.withdraw(account_number, amount)
        elif choice == 5:
            account_number = input("Enter account number: ")
            bank.calculate_interest(account_number)
        elif choice == 6:
            print("Thank you!!")
            break
        else:
            print("Invalid choice, Please try again.")


if __name__ == "__main__":
    main()
