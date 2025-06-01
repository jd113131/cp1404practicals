"""Get password insure it is valid and then display starts for each character"""

password_length = 10
password = input("Enter password: ")
while len(password) < password_length:
    print(f"Password must be at least {password_length} characters long")
    password = input("Enter password: ")

print('*' * len(password))