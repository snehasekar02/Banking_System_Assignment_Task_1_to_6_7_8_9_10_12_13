from account import Account


class Bank:
    def __init__(self):
        self.accounts = []

    def create_account(self, account_number, account_type, initial_balance):
        account = Account(account_number, account_type, initial_balance)
        self.accounts.append(account)
        return account

    def deposit(self, account_number, amount):
        for account in self.accounts:
            if account.getAccountNumber() == account_number:
                account.deposit(amount)
                break
        else:
            print("Account not found.")

    def withdraw(self, account_number, amount):
        for account in self.accounts:
            if account.getAccountNumber() == account_number:
                account.withdraw(amount)
                break
        else:
            print("Account not found.")

    def calculate_interest(self, account_number):
        for account in self.accounts:
            if account.getAccountNumber() == account_number:
                if account.getAccountType().lower() == "savings":
                    interest = account.calculate_interest()
                    new_account_balance = account.getAccountBalance() + interest
                    account.setAccountBalance(new_account_balance)
                    print(f"Your new account balance after adding interest is {account.getAccountBalance()}")
                else:
                    print("Interest calculation is only applicable for savings accounts.")
                break
        else:
            print("Account not found.")


def main():
    bank = Bank()

    account1 = bank.create_account("34567890123", "Savings", 1000.0)
    account2 = bank.create_account("98765432123", "Current", 5000.0)

    # account1.displayAccountInfo()
    # account2.displayAccountInfo()

    # print(bank.accounts)

    bank.deposit("34567890123", 2000.0)
    bank.withdraw("98765432123", 2000.0)

    bank.calculate_interest("34567890123")
    bank.calculate_interest("98765432123")


if __name__ == "__main__":
    main()
