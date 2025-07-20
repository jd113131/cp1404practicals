"""Read and store all guitar objects as a list."""

from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    guitars = read_guitar_file(FILENAME)
    guitars.sort()
    for guitar in guitars:
        print(guitar)


def read_guitar_file(filename):
    """Read a file and return a list of all guitars stored in file as Guitar class"""
    guitars = []
    with open(filename, 'r') as infile:
        for line in infile:
            parts = line.split(',')
            parts[1] = int(parts[1])
            parts[2] = float(parts[2])
            guitar = Guitar(*parts)
            guitars.append(guitar)
    return guitars


main()
