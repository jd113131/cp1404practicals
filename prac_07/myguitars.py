"""Read and store all guitar objects as a list."""

from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Get guitars form csv file add new guitars and save them back to the file."""
    guitars = read_guitar_file(FILENAME)
    guitars.sort()
    for guitar in guitars:
        print(guitar)
    guitars = add_new_guitars(guitars)
    add_guitars_to_file(FILENAME, guitars)


def read_guitar_file(filename):
    """Read a file and return a list of all guitars stored in file as Guitar class."""
    guitars = []
    with open(filename, 'r') as infile:
        for line in infile:
            parts = line.split(',')
            parts[1] = int(parts[1])
            parts[2] = float(parts[2])
            guitar = Guitar(*parts)
            guitars.append(guitar)
    return guitars


def add_new_guitars(guitars):
    """Get new guitars from user and add them to the list of guitars."""
    print("New Guitars")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(new_guitar)
        name = input("Name: ")
    return guitars


def add_guitars_to_file(filename, guitars):
    """Write guitars to file"""
    with open(filename, 'w') as outfile:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=outfile)


main()
