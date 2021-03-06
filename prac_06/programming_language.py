class ProgrammingLanguage:

    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return "{}, {} typing, Reflection={}, First append in {}".format(self.field,
                                                                         self.typing, self.reflection, self.year)

    def is_dynamic(self):
        return self.typing == "Dynamic"
