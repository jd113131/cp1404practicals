"""
Converts between temperature systems
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    """Terminal interface for converting between temperature systems"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            convert_celsius_to_fahrenheight()
        elif choice == "F":
            convert_fahrenheight_to__celsius()
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_fahrenheight_to__celsius():
    """Converts Fahrenheit to Celsius"""
    fahrenheit = float(input("fahrenheit: "))
    celsius = (fahrenheit - 32) * 5.0 / 9
    print(f"Result: {celsius:.2f} F")


def convert_celsius_to_fahrenheight():
    """Converts Celsius to Fahrenheit"""
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    print(f"Result: {fahrenheit:.2f} F")


main()
