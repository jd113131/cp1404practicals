"""Create a class for guitars."""

import datetime

class Guitar:
    """Class that stores information about a guitar"""
    def __init__(self, name="", year=0, cost=0):
        """Set up the guitar class"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of the guitar"""
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        """Return the age of the guitar"""
        return datetime.date.today().year - self.year

    def is_vintage(self):
        """Return True if the guitar is 50 or more years old (>=50)"""
        return self.get_age() >= 50

    def __lt__(self, other):
        """Return True if the guitar is newer than the other guitar"""
        return self.get_age() < other.get_age()
