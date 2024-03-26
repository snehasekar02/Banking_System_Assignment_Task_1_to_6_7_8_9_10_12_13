"""
Create a program that simulates an ATM transaction. Display options such as "Check Balance,"
"Withdraw," "Deposit,". Ask the user to enter their current balance and the amount they want to
withdraw or deposit. Implement checks to ensure that the withdrawal amount is not greater than the
available balance and that the withdrawal amount is in multiples of 100 or 500. Display appropriate
messages for success or failure.
"""
current_balance = int(input("Enter your current balance: "))
print("ATM Transaction\n1.Check Balance\n2.Withdraw\n3.Deposit\n4.Quit")
n = int(input("Enter the option for ATM transaction: "))
while n != 4:
    if n == 1:
        print("Current Balance is ", current_balance)
    elif n == 2:
        amt = int(input("Enter your Withdrawal amount: "))
        if amt < current_balance:
            if amt % 100 == 0 or amt % 500 == 0:
                current_balance -= amt
                print("Successful Withdrawal")
            else:
                print("Failure Withdrawal")
        else:
            print("Failure Withdrawal")
    elif n == 3:
        amt = int(input("Enter your Deposit amount: "))
        current_balance += amt
        print("Successful Deposit")
    print("Enter 4 to quit else")
    n = int(input("Enter the option to continue: "))
