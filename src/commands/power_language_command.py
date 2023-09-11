from src.commands.command import Command

class CalculatePowerCommand(Command):
    def __init__(self, payload, power):
        self._payload = payload
        self._power = power

    def execute(self):
        return self._payload.power(self._power)

