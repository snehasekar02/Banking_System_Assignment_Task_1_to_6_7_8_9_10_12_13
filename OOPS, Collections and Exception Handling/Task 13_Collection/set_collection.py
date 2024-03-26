from abc import ABC, abstractmethod
from typing import List, Set


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

    def get_customer_id(self) -> int:
        return self.customer_id

    def set_customer_id(self, customer_id: int):
        self.customer_id = customer_id

    def get_first_name(self) -> str:
        return self.first_name

    def set_first_name(self, first_name: str):
        self.first_name = first_name

    def get_last_name(self) -> str:
        return self.last_name

    def set_last_name(self, last_name: str):
        self.last_name = last_name

    def get_email(self) -> str:
        return self.email

    def set_email(self, email: str):
        self.email = email

    def get_phone(self) -> str:
        return self.phone

    def set_phone(self, phone: str):
        self.phone = phone

    def get_address(self) -> str:
        return self.address

    def set_address(self, address: str):
        self.address = address

    def __str__(self) -> str:
        return (f"Customer ID: {self.customer_id}\nName: {self.first_name} {self.last_name}\nEmail: "
                f"{self.email}\nPhone: {self.phone}\nAddress: {self.address}")


class Account:
    last_acc_no = 1000

    def __init__(self, account_type: str, balance: float, customer: Customer):
        self.overdraft_limit = 1000
        Account.last_acc_no += 1
        self.account_number = Account.last_acc_no
        self.account_type = account_type
        self.balance = balance
        self.customer = customer

    def get_account_number(self) -> int:
        return self.account_number

    def set_account_number(self, account_number: int):
        self.account_number = account_number

    def get_account_type(self) -> str:
        return self.account_type

    def set_account_type(self, account_type: str):
        self.account_type = account_type

    def get_balance(self) -> float:
        return self.balance

    def set_balance(self, balance: float):
        self.balance = balance

    def get_customer(self) -> Customer:
        return self.customer

    def set_customer(self, customer: Customer):
        self.customer = customer

    def __str__(self) -> str:
        return (f"Account Details:\nAccount Number: {self.account_number}\nAccount Type: {self.account_type}\nBalance: "
                f"{self.balance}\nCustomer Details:\n{self.customer}")


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
        """Set implementation"""
        self.accounts: Set[Account] = set()

    def create_account(self, customer: Customer, accType: str,
                       balance: float) -> CurrentAccount | SavingsAccount | None:
        new_account = None
        if accType is None:
            raise NullPointerException("Account Type cannot be None")
        if accType == "Savings":
            new_account = SavingsAccount(balance, customer, 4.50)
        elif accType == "Current":
            new_account = CurrentAccount(balance, customer, 1000)

        self.accounts.add(new_account)
        return new_account

    def list_accounts(self) -> List[Account]:
        return sorted(self.accounts, key=lambda acc: acc.customer.customer_id)

    def deposit(self, account_number: int, amount: float):
        if account_number is None:
            raise NullPointerException("Account number cannot be None")

        account = self.find_account(account_number)
        if account is None:
            print("Account not found.")
        else:
            account.balance += amount
            print(f"Rs.{amount} deposited successfully!!")
            print(f"The New Balance is {account.balance}")

    def withdraw(self, account_number: int, amount: float):
        if account_number is None:
            raise NullPointerException("Account number cannot be None")

        account = self.find_account(account_number)
        if account is None:
            print("Account not found.")
        elif not self.has_sufficient_funds(account_number, amount):
            raise InsufficientFundException("Insufficient funds in the account")
        else:
            account.balance -= amount
            print(f"Rs.{amount} withdrawn successfully!!")
            print(f"The New Balance is {account.balance}")

    def transfer(self, from_account_number: int, to_account_number: int, amount: float):
        if from_account_number is None or to_account_number is None:
            raise NullPointerException("Account numbers cannot be None")

        from_account = self.find_account(from_account_number)
        to_account = self.find_account(to_account_number)

        if from_account is None or to_account is None:
            print("One or both accounts not found.")
        elif not self.has_sufficient_funds(from_account_number, amount):
            raise InsufficientFundException("Insufficient funds in the account")
        else:
            from_account.balance -= amount
            to_account.balance += amount
            print("Successful transfer")

    def withdraw_from_current_account(self, account_number: int, amount: float):
        if account_number is None:
            raise NullPointerException("Account number cannot be None")

        account = self.find_account(account_number)
        if account is None:
            print("Account not found.")
        elif not self.is_overdraft_limit_exceeded(account_number, amount):
            raise OverDraftLimitExceededException("Overdraft limit exceeded")

    def find_account(self, account_number: int):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

    def has_sufficient_funds(self, account_number: int, amount: float):
        account = self.find_account(account_number)
        if account is None:
            return False
        return account.balance >= amount

    def is_overdraft_limit_exceeded(self, account_number: int, amount: float):
        account = self.find_account(account_number)
        if isinstance(account, CurrentAccount):
            max_withdrawal = account.balance + account.overdraft_limit
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

        print(bank.list_accounts())

        for account in bank.list_accounts():
            print(str(account))

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
