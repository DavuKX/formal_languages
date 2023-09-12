from src.entities.set_operations import SetOperations
from src.commands.command import Command


class DisplayOperationResultCommand(Command):
    def __init__(self, result=None):
        self.result = result

    def execute(self):
        if isinstance(self.result, int):
            print(self.result)
        else:
            print(self.result.get_values())

    def set_result(self, result: SetOperations):
        self.result = result
        return self

    def get_result(self):
        return self.result
