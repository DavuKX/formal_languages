from src.commands.command import Command
from src.entities.language import Language as Lenguage


class CalculateConcatenationCommand(Command):
    def __init__(self, payload):
        self._payload = payload

    def execute(self):
        result = Lenguage(set())
        result = result.concatenation(self._payload)
        return result
