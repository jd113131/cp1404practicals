"""Taxi simulator."""
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MAIN_MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Menu program that allows users to add taxi rides."""
    current_taxi = None
    cost = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")
    print(MAIN_MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            current_taxi = select_taxi(taxis, current_taxi)
        elif choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                cost += taxi_ride(taxis, current_taxi)
            pass
        else:
            print("Invalid option")

        print(f"Bill to date: ${cost:.2f}")
        print(MAIN_MENU)
        choice = input(">>> ").lower()

    print(f"Total trip cost: ${cost}")
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    """Display the taxis information."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def taxi_ride(taxis, current_taxi):
    distance = int(input("Drive how far? "))
    taxis[current_taxi].drive(distance)
    price = taxis[current_taxi].get_fare()
    taxis[current_taxi].start_fare()  # reset for next time
    return price


def select_taxi(taxis, old_taxi):
    """Select a taxi based on user choice."""
    print("Taxis available:")
    display_taxis(taxis)
    try:
        current_taxi = int(input("Choose taxi: "))
        if 0 <= current_taxi < len(taxis):
            return current_taxi
    except ValueError:
        pass
    print("Invalid option")
    return old_taxi


main()
