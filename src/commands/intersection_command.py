import copy
from src.commands.command import Command


class IntersectionCommand(Command):
    def __init__(self, payload) -> None:
        self._payload = list(payload)

    def execute(self):
        result = copy.deepcopy(self._payload[0])

        for i in range(1, len(self._payload)):
            result = result.intersection(self._payload[i].get_values())

        return result
