from src.commands.command import Command
from src.entities.alphabet import Alphabet

class GenerateLanguagesCommand(Command):
    def __init__(self, payload, simbols_number,max_word_length) -> None:
        self._payload = list(payload)
        self._simbols_number = simbols_number
        self._max_word_length = max_word_length

    def execute(self):
        languages = Alphabet(set())
        languages = languages.generate_language(self._simbols_number, self._max_word_length)
        return languages
        
     