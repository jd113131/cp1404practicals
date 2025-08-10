"""Create a project management class."""

import datetime

class Project:
    """Create project class."""
    def __init__(self, name="",
                 start_date="",
                 priority=0,
                 cost_estimate=0.0,
                 completion_percentage=0):
        """initialises project class."""
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """String representation of project class."""
        return (f"{self.name}, "
                f"start: {self.start_date.strftime("%d/%m/%Y")}, "
                f"priority {self.priority}, "
                f"estimate: ${self.cost_estimate}, "
                f"completion: {self.completion_percentage}%")

    def __repr__(self):
        """String representation of project class when returned in list."""
        return self.__str__()

    def __lt__(self, other):
        """Returns true if the priority is less than the second project."""
        return self.priority < other.priority

    def is_complete(self):
        """Returns true if the project is complete."""
        return self.completion_percentage == 100

    def starts_after(self, date):
        """Returns true if the project starts after the given date."""
        return self.start_date > date
