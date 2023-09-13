from src.commands.command import Command
from src.entities.language import Language


class CalculateInverseCommand(Command):
    def __init__(self, payload):
        self._payload = payload

    def execute(self):
        inverse_values = set()
        for word in self._payload.get_values():
            inverse_values.add(word[::-1])
        return Language(inverse_values)
