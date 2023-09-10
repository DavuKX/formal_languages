from command import Command

class Cardinality(Command):
    def __init__(self, language_a, language_b):
        self.language_a = language_a
        self.language_b = language_b

    def execute(self):
        return self.language_a.cardinality()