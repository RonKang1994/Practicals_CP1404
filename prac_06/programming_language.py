class ProgrammingLanguage:
    """Represent a Programming language object."""
    def __init__(self, field="", typing="Dynamic", dynamic=True, year=2000):
        """Initialise a Language instance."""
        self.field = field
        if typing.lower() == "dynamic" or typing.lower() == "static":
            self.typing = typing
        else:
            self.typing = "UNKNOWN"
        self.dynamic = dynamic
        self.year = year

    def is_dynamic(self):
        if self.typing.lower() == "dynamic":
            return True
        else:
            return False

    def __str__(self):
        return("{}, {} Typing, Reflection = {}, first appeared in {}".format(str(self.field), str(self.typing), str(self.dynamic), str(self.year)))
