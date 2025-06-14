"""Get a list of numbers and display significant information"""
NUMBER_OF_NUMBERS = 5

def main():
    """Find information about imputed numbers"""
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    check_user(usernames)
    numbers = []
    get_numbers(numbers)
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The largest number is {sum(numbers)/len(numbers)}")


def get_numbers(numbers):
    """Get a list of numbers"""
    for i in range(NUMBER_OF_NUMBERS):
        is_valid_number = False
        while not is_valid_number:
            try:
                numbers.append(int(input("Number: ")))
                is_valid_number = True
            except ValueError:
                print("Invalid input")

def check_user(usernames):
    """Check if a user is in the list of usernames"""
    username_found = False
    while not username_found:
        user = input("Username: ")
        if user in usernames:
            print("Access granted")
            username_found = True
        else:
            print("Access denied")

main()
