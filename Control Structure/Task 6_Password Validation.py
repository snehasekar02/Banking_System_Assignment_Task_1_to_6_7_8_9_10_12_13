"""
Task 6: Password Validation
Create a program that maintains a list of bank transactions (deposits and withdrawals)
for a customer. Use a while loop to allow the user to keep adding transactions
until they choose to exit. Display the transaction history upon exit using looping statements.
"""
transaction_history = []
current_balance = 0
while True:
    print("1.Deposit\n2.Withdraw\n3.Exit\n")
    n = int(input("enter your choice: "))
    if n == 1:
        amt = int(input("enter the amount to deposit: "))
        current_balance += amt
        print(current_balance)
        transaction_history.append(["Deposit", amt])
        print(amt, " successfully deposited")
    elif n == 2:
        amt = int(input("enter the amount to withdraw: "))
        print(current_balance)
        if amt <= current_balance:
            print(amt, " successfully withdrawn")
            current_balance -= amt
            transaction_history.append(["Withdraw", amt])
        else:
            print("insufficient balance")
    elif n == 3:
        for i in range(0, len(transaction_history)):
            print(str(i + 1), ".", transaction_history[i][0], ":", transaction_history[i][1])
        break
    else:
        print("Invalid Choice")
