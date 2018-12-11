import datetime

class Guitar:
    """Guitar Class"""
    def __init__(self, name="", year=2000, cost=1000):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return("Guitar : {} ({}) : ${:.2f}".format(self.name, str(self.year), self.cost))

    def get_age(self):
        age = datetime.datetime.now().year - self.year
        return age

    def is_vintage(self):
        if self.get_age() > 50:
            return True
        else:
            return False