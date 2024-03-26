"""
You are responsible for calculating compound interest on savings accounts for bank customers. You
need to calculate the future balance for each customer's savings account after a certain number of years.
Tasks:
1. Create a program that calculates the future balance of a savings account.
2. Use a loop structure (e.g., for loop) to calculate the balance for multiple customers.
3. Prompt the user to enter the initial balance, annual interest rate, and the number of years.
4. Calculate the future balance using the formula:
future_balance = initial_balance * (1 + annual_interest_rate/100)^years.
5. Display the future balance for each customer.
"""
n = int(input("Enter the no of bank customers: "))
for i in range(1, n + 1):
    initial_balance = int(input("Enter the initial balance for customer " + str(i) + ": "))
    annual_interest_rate = int(input("Enter the annual interest rate for customer " + str(i) + ": "))
    years = int(input("Enter the no of years for customer " + str(i) + ": "))
    future_balance = initial_balance * (1 + annual_interest_rate / 100) ** years
    print("The future balance for customer ", i, " is ", future_balance)
