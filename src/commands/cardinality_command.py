from src.commands.command import Command



class CalculateCardinalityCommand(Command):
    def __init__(self, payload):
        self._payload = payload

    def execute(self):
        return self._payload.cardinality()
