from src.commands.command import Command
from src.entities.alphabet import Alphabet
from src.entities.language import Language


class GenerateLanguagesCommand(Command):
    def __init__(self, payload, simbols_number, max_word_length) -> None:
        self._payload = payload
        self._simbols_number = simbols_number
        self._max_word_length = max_word_length

    def execute(self):
        alphabet = self._payload
        alphabet = alphabet.generate_language(self._simbols_number, self._max_word_length)

        return Language(alphabet.get_values())
