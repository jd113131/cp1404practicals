"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        if result < 0 or result > 100:
            print("Invalid result. Please enter a result between 0 and 100!")
        else:
            is_finished = True
    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", result)
