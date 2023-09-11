from src.commands.command import Command

class CalculateConcatenationCommand(Command):
    def __init__(self, payload):
        self._payload = payload

    def execute(self):
        result = self._payload[0]
        for language in self._payload[1:]:
            new_result = set()
            for word1 in result.get_values():
                for word2 in language.get_values():
                    new_result.add(word1 + word2)
            result.set_values(new_result)

        return result
