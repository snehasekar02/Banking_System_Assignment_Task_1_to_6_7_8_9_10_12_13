"""
Task 10: Has A Relation / Association
1. Create a `Customer` class with the following attributes:

Customer ID

First Name

Last Name

Email Address (validate with valid email address)

Phone Number (Validate 10-digit phone number)

Address

Methods and Constructor:
o Implement default constructors and overload the constructor with Account attributes, generate getter, setter,
print all information of attribute) methods for the attributes.
2. Create an `Account` class with the following attributes:

Account Number (a unique identifier).

Account Type (e.g., Savings, Current)

Account Balance

Customer (the customer who owns the account)

Methods and Constructor:
o Implement default constructors and overload the constructor with Account attributes, generate getter, setter,
(print all information of attribute) methods for the attributes.
Create a Bank Class and must have following requirements:
1. Create a Bank class to represent the banking system. It should have the following methods:

create_account(Customer customer, long accNo, String accType, float balance): Create a new bank account for the given
customer with the initial balance.

get_account_balance(account_number: long): Retrieve the balance of an account given its account number.
 should return the current balance of account.

deposit(account_number: long, amount: float): Deposit the specified amount into the account.
 Should return the current balance of account.

withdraw(account_number: long, amount: float): Withdraw the specified amount from the account.
 Should return the current balance of account.

transfer(from_account_number: long, to_account_number: int, amount: float): Transfer money from one account to another.

getAccountDetails(account_number: long): Should return the account and customer details.
2. Ensure that account numbers are automatically generated when an account is created, starting from 1001 and
incrementing for each new account.
3. Create a BankApp class with a main method to simulate the banking system. Allow the user to interact with
the system by entering commands such as "create_account", "deposit", "withdraw", "get_balance", "transfer",
"getAccountDetails" and "exit." create_account should display sub menu to choose type of accounts and
repeat this operation until user exit.
"""

import re


class Customer:
    def __init__(self, customer_id="", first_name="", last_name="", email="", phone="", address=""):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.address = address

    # Getter and setter methods for Customer attributes
    def get_customer_id(self):
        return self.customer_id

    def set_customer_id(self, customer_id):
        self.customer_id = customer_id

    def get_first_name(self):
        return self.first_name

    def set_first_name(self, first_name):
        self.first_name = first_name

    def get_last_name(self):
        return self.last_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_phone(self):
        return self.phone

    def set_phone(self, phone):
        self.phone = phone

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    # Method to print all information of attributes
    def display_info(self):
        print("Customer ID:", self.customer_id)
        print("First Name:", self.first_name)
        print("Last Name:", self.last_name)
        print("Email Address:", self.email)
        print("Phone Number:", self.phone)
        print("Address:", self.address)


class Account:
    account_number_generator = 1000

    def __init__(self, customer, account_type, balance):
        self.account_number = Account.generate_account_number()
        self.customer = customer
        self.account_type = account_type
        self.balance = balance

    @classmethod
    def generate_account_number(cls):
        cls.account_number_generator += 1
        return cls.account_number_generator

    # Getter and setter methods for Account attributes
    def get_account_number(self):
        return self.account_number

    def set_account_number(self, account_number):
        self.account_number = account_number

    def get_account_type(self):
        return self.account_type

    def set_account_type(self, account_type):
        self.account_type = account_type

    def get_account_balance(self):
        return self.balance

    def set_account_balance(self, balance):
        self.balance = balance

    def get_customer(self):
        return self.customer

    def set_customer(self, customer):
        self.customer = customer

    def display_info(self):
        print("**Account Details**")
        print("Account Number:", self.account_number)
        print("Account Type:", self.account_type)
        print("Account Balance:", self.balance)
        print("**Customer Details**")
        self.customer.display_info()


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, customer, account_type, balance):
        account = Account(customer, account_type, balance)
        self.accounts[account.get_account_number()] = account
        return account.get_account_number()

    def get_account_balance(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number].get_account_balance()
        else:
            return None

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number].set_account_balance(
                self.accounts[account_number].get_account_balance() + amount)
            return self.accounts[account_number].get_account_balance()
        else:
            return None

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if self.accounts[account_number].get_account_balance() >= amount:
                self.accounts[account_number].set_account_balance(
                    self.accounts[account_number].get_account_balance() - amount)
                return self.accounts[account_number].get_account_balance()
            else:
                return "Insufficient funds"
        else:
            return None

    def transfer(self, from_account_number, to_account_number, amount):
        if from_account_number in self.accounts and to_account_number in self.accounts:
            if self.accounts[from_account_number].get_account_balance() >= amount:
                self.accounts[from_account_number].set_account_balance(
                    self.accounts[from_account_number].get_account_balance() - amount)
                self.accounts[to_account_number].set_account_balance(
                    self.accounts[to_account_number].get_account_balance() + amount)
                return f"Transfer successful. Updated balance for account {from_account_number}: {self.accounts[from_account_number].get_account_balance()}"
            else:
                return "Insufficient funds for transfer"
        else:
            return "One or both accounts not found"

    def get_account_details(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]
        else:
            return "Account not found"


def validate_email(email):
    return re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email) is not None


def validate_phone(phone):
    return re.match(r"^\d{10}$", phone) is not None


class BankApp:
    def __init__(self):
        self.bank = Bank()

    def run(self):
        while True:
            print("------------------------------------------")
            print("\nBanking System Menu:")
            print("1. Create Account")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Transfer")
            print("5. Get Account Balance")
            print("6. Get Account Details")
            print("7. Quit")
            print("------------------------------------------")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.create_account()
            elif choice == "2":
                self.deposit()
            elif choice == "3":
                self.withdraw()
            elif choice == "4":
                self.transfer()
            elif choice == "5":
                self.get_balance()
            elif choice == "6":
                self.get_account_details()
            elif choice == "7":
                print("Thank You!!")
                break
            else:
                print("Invalid choice, Please try again!!")

    def create_account(self):
        print("\nCreate Account:")
        customer_id = input("Enter Customer ID: ")
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        email = input("Enter Email Address: ")
        while not validate_email(email):
            email = input("Invalid email address. \nEnter again: ")
        phone = input("Enter Phone Number: ")
        while not validate_phone(phone):
            phone = input("Invalid phone number. \nEnter again: ")
        address = input("Enter Address: ")
        customer = Customer(customer_id, first_name, last_name, email, phone, address)

        print("\nChoose Account Type:")
        print("1. Savings Account")
        print("2. Current Account")
        account_type = input("Enter choice - 1 or 2: ")
        while account_type not in ["1", "2"]:
            account_type = input("Invalid choice. Enter again (1 or 2): ")

        initial_balance = float(input("Enter Initial Balance: "))

        account_number = self.bank.create_account(customer, "Savings" if account_type == "1" else "Current",
                                                  initial_balance)
        print(f"Account created successfully! your Account Number is {account_number}")

    def deposit(self):
        account_number = int(input("Enter Account Number: "))
        amount = float(input("Enter Amount to Deposit: "))
        balance = self.bank.deposit(account_number, amount)
        if balance is not None:
            print(f"Deposit successful! Current Balance: {balance}")
        else:
            print("Failed to deposit. Account not found.")

    def withdraw(self):
        account_number = int(input("Enter Account Number: "))
        amount = float(input("Enter Amount to Withdraw: "))
        balance = self.bank.withdraw(account_number, amount)
        if balance is not None:
            if balance == "Insufficient funds":
                print("Failed to withdraw. Insufficient funds.")
            else:
                print(f"Withdrawal successful! Current Balance: {balance}")
        else:
            print("Failed to withdraw. Account not found.")

    def transfer(self):
        from_account_number = int(input("Enter From Account Number: "))
        to_account_number = int(input("Enter To Account Number: "))
        amount = float(input("Enter Amount to Transfer: "))
        message = self.bank.transfer(from_account_number, to_account_number, amount)
        print(message)

    def get_balance(self):
        account_number = int(input("Enter Account Number: "))
        balance = self.bank.get_account_balance(account_number)
        if balance is not None:
            print(f"Current Balance: {balance}")
        else:
            print("Account not found.")

    def get_account_details(self):
        account_number = int(input("Enter Account Number: "))
        Account.display_info(self.bank.get_account_details(account_number))
        #print(details)


if __name__ == "__main__":
    bank_app = BankApp()
    bank_app.run()
