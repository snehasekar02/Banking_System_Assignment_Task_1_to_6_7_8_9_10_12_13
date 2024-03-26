"""
1. Create an abstract class BankAccount that represents a generic bank account. It should include the following
attributes and methods:

Attributes:
o Account number.
o Customer name.
o Balance.

Constructors:
o Implement default constructors and overload the constructor with Account attributes, generate getter and setter,
 print all information of attribute methods for the attributes.

Abstract methods:
o deposit(amount: float): Deposit the specified amount into the account.
o withdraw(amount: float): Withdraw the specified amount from the account (implement error handling for
 insufficient funds).
o calculate_interest(): Abstract method for calculating interest.
"""

from abc import ABC, abstractmethod


class BankAccount(ABC):
    def __init__(self, account_number, customer_name, balance):
        self.__account_number = account_number
        self.__customer_name = customer_name
        self.__balance = balance

    def get_account_number(self):
        return self.__account_number

    def set_account_number(self, account_number):
        self.__account_number = account_number

    def get_customer_name(self):
        return self.__customer_name

    def set_customer_name(self, customer_name):
        self.__customer_name = customer_name

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        self.__balance = balance

    def display_info(self):
        print("Account Number:", self.__account_number)
        print("Customer Name:", self.__customer_name)
        print("Balance:", self.__balance)

    @abstractmethod
    def deposit(self, amount: float):
        pass

    @abstractmethod
    def withdraw(self, amount: float):
        pass

    @abstractmethod
    def calculate_interest(self):
        pass


"""
2. Create two concrete classes that inherit from BankAccount:

SavingsAccount: A savings account that includes an additional attribute for interest rate. Implement the 
calculate_interest() method to calculate interest based on the balance and interest rate.

CurrentAccount: A current account with no interest. Implement the withdraw() method to allow overdraft up to a certain
 limit (configure a constant for the overdraft limit).
"""


class SavingsAccount(BankAccount):
    interest_rate = 4.50

    def __init__(self, account_number, customer_name, balance):
        super().__init__(account_number, customer_name, balance)

    def calculate_interest(self):
        interest_amount = (self.get_balance() * self.interest_rate) / 100
        self.set_balance(self.get_balance() + interest_amount)
        print(f"Interest Amount is {interest_amount}")
        print(f"The New Balance with interest is {self.get_balance()}")

    def deposit(self, amount: float):
        self.set_balance(self.get_balance() + amount)
        print(f"Rs.{amount} deposited successfully")
        print(f"The New Balance is {self.get_balance()}")

    def withdraw(self, amount: float):
        if amount > self.get_balance():
            print("Insufficient balance.")
        else:
            self.set_balance(self.get_balance() - amount)
            print(f"Rs.{amount} withdrawn successfully")
            print(f"The New Balance is {self.get_balance()}")


class CurrentAccount(BankAccount):
    OVERDRAFT_LIMIT = 1500.0

    def deposit(self, amount: float):
        self.set_balance(self.get_balance() + amount)
        print(f"Rs.{amount} deposited successfully")
        print(f"The New Balance is {self.get_balance()}")

    def withdraw(self, amount: float):
        available_balance = self.get_balance() + self.OVERDRAFT_LIMIT
        if amount > available_balance:
            print("Withdrawal amount exceeds available balance and overdraft limit.")
        else:
            self.set_balance(self.get_balance() - amount)
            print(f"Rs.{amount} withdrawn successfully")
            print(f"The New Balance is {self.get_balance()}")

    def calculate_interest(self):
        pass


class Bank:
    def __init__(self):
        self.__accounts = []

    def create_account(self, account_type):
        account_number = input("Enter account number: ")
        customer_name = input("Enter customer name: ")
        initial_balance = float(input("Enter initial balance: "))
        if account_type == "1":
            account = SavingsAccount(account_number, customer_name, initial_balance)
        elif account_type == "2":
            account = CurrentAccount(account_number, customer_name, initial_balance)
        else:
            print("Invalid account type.")
            return
        self.__accounts.append(account)
        print("Account created successfully.")

    def deposit(self, account_number, amount):
        for account in self.__accounts:
            if account.get_account_number() == account_number:
                account.deposit(amount)
                return
        print("Account not found.")

    def withdraw(self, account_number, amount):
        for account in self.__accounts:
            if account.get_account_number() == account_number:
                account.withdraw(amount)
                return
        print("Account not found.")

    def calculate_interest(self, account_number):
        for account in self.__accounts:
            if account.get_account_number() == account_number:
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
        choice = input("Enter your choice: ")
        print("------------------------------------------")

        if choice == "1" or choice == "2":
            bank.create_account(choice)
        elif choice == "3":
            account_number = input("Enter account number: ")
            amount = float(input("Enter deposit amount: "))
            bank.deposit(account_number, amount)
        elif choice == "4":
            account_number = input("Enter account number: ")
            amount = float(input("Enter withdrawal amount: "))
            bank.withdraw(account_number, amount)
        elif choice == "5":
            account_number = input("Enter account number: ")
            bank.calculate_interest(account_number)
        elif choice == "6":
            print("Thank You!!")
            break
        else:
            print("Invalid choice, Please try again.")


if __name__ == "__main__":
    main()
