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

    def deposit(self,amount : float):
        if amount > 0:
            self.__accountBalance += amount
            print(f"Rs.{amount} deposited successfully")
            print(f"Your new balance is {self.__accountBalance}")
        else:
            print("Please enter valid amount to deposit!!")

    def withdraw(self, amount : float):
        if self.__accountBalance > amount:
            self.__accountBalance -= amount
            print(f"Rs.{amount} withdrawn successfully")
            print(f"Your new balance is {self.__accountBalance}")
        else:
            print("Insufficient Balance!!")

    def calculate_interest(self) -> float:
        interest_rate = 4.5
        interest_amount = (self.__accountBalance * interest_rate)/100
        return interest_amount






