"""Get password insure it is valid and then display starts for each character"""

def main():
    password_length = 10
    password = get_password(password_length)

    display_masked_password(password)


def display_masked_password(password, s='*'):
    print(s * len(password))


def get_password(password_length):
    password = input("Enter password: ")
    while len(password) < password_length:
        print(f"Password must be at least {password_length} characters long")
        password = input("Enter password: ")
    return password


main()