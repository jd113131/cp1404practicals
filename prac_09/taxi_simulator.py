"""Taxi simulator."""
from prac_01.temperatures import choice

MAIN_MENU = "q)uit, c)hoose taxi, d)rive"

def main():
    """Menu program that allows users to add taxi rides."""
    current_taxi = None
    taxis = []
    print("Let's drive!")
    print(MAIN_MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            # TODO add choose logic
            pass
        elif choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                # TODO add logic
                pass
            pass
        else:
            print("Invalid option")


        print(MAIN_MENU)
        choice = input(">>> ").lower()

    # TODO final message
    print()

main()