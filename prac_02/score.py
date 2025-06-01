"""
Determine score status
"""

import random

def main():
    """Generates and displays score status"""
    score = float(input("Enter score: "))
    result = determin_result(score)
    print(result)
    score = random.randrange(0,101)
    result = determin_result(score)
    print(result)

def determin_result(score):
    """Returns score status"""
    if score < 0:
        return "Invalid score"
    elif score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    elif score <= 100:
        return "Excellent"
    return "Invalid score"

main()
