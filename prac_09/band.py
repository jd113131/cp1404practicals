"""Band class"""

class Band():
    """Band class"""
    def __init__(self, name: str):
        """Construct a Band object."""
        self.name = name
        self.musicians = []

    def add(self, musician):
        """Add a musician."""
        self.musicians.append(musician)

    def __str__(self):
        """String representation of Band class."""
        return (f"{self.name}"
                f"{[str(musician) for musician in self.musicians]}"")")

    def play(self):
        """Play the band."""
        for musician in self.musicians:
            print(musician.play())
