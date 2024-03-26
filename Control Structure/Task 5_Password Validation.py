"""
Task 5: Password Validation
Write a program that prompts the user to create a password for their bank account. Implement if conditions to validate the password according to these rules:

The password must be at least 8 characters long.

It must contain at least one uppercase letter.

It must contain at least one digit.

Display appropriate messages to indicate whether their password is valid or not.
"""
password = input("Enter the password for bank account: ")
length = len(password)
u_c = 0
d_c = 0
for i in password:
    if i.isupper():
        u_c += 1
    elif i.isdigit():
        d_c += 1
if length >= 8 and u_c >= 1 and d_c >= 1:
    print("password is valid")
else:
    print("password is invalid")
