"""Create a project management class"""

class Project:
    def __init__(self, name="", start_date="", priority=0, cost_estimate=0.0,completion_percentage=0.0):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        return f"{self.name}, {self.start_date}, {self.priority}, {self.cost_estimate}, {self.completion_percentage}"

    def __repr__(self):
        return '('+self.__str__()+"\n)"

