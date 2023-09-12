from src.commands.command import Command


class ValidateLambdaCommand(Command):
    def __init__(self, has_lambda = False) -> None:
        self._has_lambda = has_lambda
        self._language = None

    def set_language(self, language):
        self._language = language
        return self

    def get_language(self):
        return self._language

    def execute(self):
        if self._language.has_lambda():
            self._has_lambda = True
            self.set_language(self._language.get_values().remove('#'))
        return self._has_lambda


