"""Create a project management class"""

import datetime

class Project:
    def __init__(self, name="", start_date="", priority=0, cost_estimate=0.0, completion_percentage=0):
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        return (f"{self.name}, "
                f"start: {self.start_date.strftime("%d/%m/%Y")}, "
                f"priority {self.priority}, "
                f"estimate: {self.cost_estimate}, "
                f"completion: {self.completion_percentage}%")

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        return self.priority < other.priority

    def is_complete(self):
        return self.completion_percentage == 100

    def starts_after(self, date):
        return self.start_date > date
