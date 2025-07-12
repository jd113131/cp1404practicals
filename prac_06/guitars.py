"""
Guitars Class exercises
Estimate: 45:00 minutes
Actual: 48:50 minutes
"""
from prac_06.guitar import Guitar


def main():
    print("My guitars!")
    guitars = []
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(new_guitar)
        name = input("Name: ")

    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}"
              f"{" (vintage)" if guitar.is_vintage() else ""}")




main()
