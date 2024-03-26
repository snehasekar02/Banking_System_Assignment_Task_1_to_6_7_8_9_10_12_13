"""
Task 4: Looping, Array and Data Validation
You are tasked with creating a program that allows bank customers to check their account balances. The program should handle multiple customer accounts, and the customer should be able to enter their account number, balance to check the balance.
Tasks:
1. Create a Python program that simulates a bank with multiple customer accounts.
2. Use a loop (e.g., while loop) to repeatedly ask the user for their account number and balance until they enter a valid account number.
3. Validate the account number entered by the user.
4. If the account number is valid, display the account balance. If not, ask the user to try again.
"""
customer_account = [10012233, 10024455, 10037788, 10048798, 10057453]
while True:
    acc_no = int(input("Enter the account number of a customer: "))
    balance = int(input("Enter the account balance of a customer: "))
    if acc_no in customer_account:
        print("The account balance is ", balance)
        break
    else:
        print("Invalid account number, Try again!!")
        continue
