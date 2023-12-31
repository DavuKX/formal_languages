from src.commands.command import Command
from src.entities.language import Language


class CalculateCardinalityCommand(Command):
    def __init__(self, payload):
        self._payload = payload

    def execute(self):
        return self._payload.cardinality()
