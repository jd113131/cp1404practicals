"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
On lune 13 or 14 when converting user input into a integer if non-numbers where used
2. When will a ZeroDivisionError occur?
If 0 was entered for the denominator
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes you can yous LBYl and uses a while loop to prompt for new input until a non-zero integer is entered
# there was a error with the commit this is a comment to test
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Cannot divide by zero!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")