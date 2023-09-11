from src.commands.command import Command
from src.commands.union_command import UnionCommand


class KleeneClosureCommand(Command):
    def __init__(self, payload, simbols_number,max_word_length) -> None:
        self._payload = list(payload)
        self._simbols_number = simbols_number
        self._max_word_length = max_word_length

    def execute(self):
        joined_alphabets = UnionCommand(self._payload).execute()
        return joined_alphabets.generate_words_with_kleene_closure(self._simbols_number,self._max_word_length)
