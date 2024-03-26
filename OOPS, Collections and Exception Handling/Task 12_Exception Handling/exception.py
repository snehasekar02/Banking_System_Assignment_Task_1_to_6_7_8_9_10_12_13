from abc import ABC, abstractmethod
from typing import List, Dict


class InsufficientFundException(Exception):
    pass


class InvalidAccountException(Exception):
    pass


class OverDraftLimitExceededException(Exception):
    pass


class NullPointerException(Exception):
    pass


class Customer:
    def __init__(self, customer_id: int, first_name: str, last_name: str, email: str, phone: str, address: str):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.address = address


class Account:
    last_acc_no = 1000

    def __init__(self, account_type: str, balance: float, customer: Customer):
        self.overdraft_limit = 1000
        Account.last_acc_no += 1
        self.account_number = Account.last_acc_no
        self.account_type = account_type
        self.balance = balance
        self.customer = customer


class SavingsAccount(Account):
    def __init__(self, account_balance: float, customer: Customer, interest_rate: float):
        super().__init__("Savings", account_balance, customer)
        self.interest_rate = interest_rate


class CurrentAccount(Account):
    def __init__(self, account_balance: float, customer: Customer, overdraft_limit: float):
        super().__init__("Current", account_balance, customer)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount: float):
        if self.balance + self.overdraft_limit < amount:
            raise OverDraftLimitExceededException("Overdraft limit exceeded")
        else:
            self.balance -= amount
            return f"Withdrawal successful. Updated balance: {self.balance}"


class IBankServiceProvider(ABC):
    @abstractmethod
    def create_account(self, customer: Customer, accType: str, balance: float) -> int:
        pass


class HMBank(IBankServiceProvider):
    def __init__(self):
        self.accounts: Dict[int, Account] = {}

    def create_account(self, customer: Customer, accType: str, balance: float) -> int:
        new_account = None
        if accType is None:
            raise NullPointerException("Account Type cannot be None")
        if accType == "Savings":
            new_account = SavingsAccount(balance, customer, 4.50)
        elif accType == "Current":
            new_account = CurrentAccount(balance, customer, 1000)

        self.accounts[new_account.account_number] = new_account
        # print(self.accounts)
        return new_account.account_number

    def deposit(self, account_number: int, amount: float):
        if account_number is None:
            raise NullPointerException("Account number cannot be None")
        if account_number in self.accounts:
            self.accounts[account_number].balance += amount
            print(f"Rs.{amount} deposited successfully!!")
            print(f"The New Balance is {self.accounts[account_number].balance}")

    def withdraw(self, account_number: int, amount: float):
        if not self.has_sufficient_funds(account_number, amount):
            raise InsufficientFundException("Insufficient funds in the account")
        else:
            self.accounts[account_number].balance -= amount
            print(f"Rs.{amount} withdrawn successfully!!")
            print(f"The New Balance is {self.accounts[account_number].balance}")

    def transfer(self, from_account_number: int, to_account_number: int, amount: float):
        if not self.is_valid_account(from_account_number) or not self.is_valid_account(to_account_number):
            raise InvalidAccountException("Invalid account number")

        if not self.has_sufficient_funds(from_account_number, amount):
            raise InsufficientFundException("Insufficient funds in the account")
        else:
            self.accounts[from_account_number].balance -= amount
            self.accounts[to_account_number].balance += amount
            print("Successful transfer")

    def withdraw_from_current_account(self, account_number: int, amount: float):
        if not self.is_overdraft_limit_exceeded(account_number, amount):
            raise OverDraftLimitExceededException("Overdraft limit exceeded")

    def has_sufficient_funds(self, account_number: int, amount: float):
        if account_number not in self.accounts:
            return False
        return self.accounts[account_number].balance >= amount

    def is_valid_account(self, account_number: int):
        return account_number in self.accounts

    def is_overdraft_limit_exceeded(self, account_number: int, amount: float):
        if account_number in self.accounts and isinstance(self.accounts[account_number], CurrentAccount):
            max_withdrawal = self.accounts[account_number].balance + self.accounts[account_number].overdraft_limit
            return amount < max_withdrawal
        return False


def main():
    bank = HMBank()

    try:
        c1 = Customer(1, "sneha", "c", "csneha@gmail.com", "9025309801", "Trichy, TamilNadu")
        a1 = HMBank.create_account(bank, c1, "Savings", 2000)

        c2 = Customer(2, "suba", "g", "gsuba@gmail.com", "8248820824", "Trichy, TamilNadu")
        a2 = HMBank.create_account(bank, c2, "Current", 4000)

        c3 = Customer(3, "pavi", "r", "pavir@gmail.com", "8247720824", "Trichy, TamilNadu")
        a2 = HMBank.create_account(bank, c3, "Current", 6000)

        bank.deposit(1001, 1000)

    except NullPointerException as e:
        print("Error:", e)

    # bank.deposit(1001, 1000)

    try:
        bank.withdraw(1001, 1000)
    except InsufficientFundException as e:
        print("Error:", e)

    try:
        bank.transfer(1001, 1002, 500)
    except InsufficientFundException as e:
        print("Error:", e)
    except InvalidAccountException as e:
        print("Error:", e)

    try:
        bank.withdraw_from_current_account(1002, 10)
    except OverDraftLimitExceededException as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
