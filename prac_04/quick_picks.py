"""Generate quick picks numbers"""
import random

NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45


def main():
    """Quick pick program generates a set of 6 random numbers"""
    number_of_quick_picks = int(input("How many quick picks? "))
    while number_of_quick_picks < 0:
        print("Please enter a number greater than 0")
        number_of_quick_picks = int(input("How many quick picks? "))

    for i in range(number_of_quick_picks):
        quick_pick = []
        for j in range(NUMBERS_PER_LINE):
            quick_pick_number = random.randint(MINIMUM, MAXIMUM)
            while quick_pick_number in quick_pick:
                quick_pick_number = random.randint(MINIMUM, MAXIMUM)
            quick_pick.append(quick_pick_number)
        quick_pick.sort()
        print(' '.join(f'{number:2}' for number in quick_pick))


main()
