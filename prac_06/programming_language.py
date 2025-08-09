"""Programming Language class"""

class ProgrammingLanguage:
    """Representation of information about the programming language"""
    def __init__(self, language, typing = "Static", reflection = True, year = 0):
        """Construct the programming language class"""
        self.language = language
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return sting formating for ProgrammingLanguage"""
        return f"{self.language}, {self.typing } Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Return True if this programming language is dynamic"""
        return self.typing == "Dynamic"
