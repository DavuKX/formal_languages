from src.commands.command import Command
from src.commands.difference_command import DifferenceCommand
from src.commands.intersection_command import IntersectionCommand
from src.commands.kleene_closure_command import KleeneClosureCommand
from src.commands.union_command import UnionCommand
from src.commands.concatenation_language_command import CalculateConcatenationCommand
from src.commands.power_language_command import CalculatePowerCommand
from src.commands.inverse_language_command import CalculateInverseCommand
from src.commands.cardinality_command import CalculateCardinalityCommand
from src.commands.generate_languages_command import GenerateLanguagesCommand


class Invoker:
    _on_start = None
    _on_finish = None
    actions = {
        'union': UnionCommand,
        'difference': DifferenceCommand,
        'intersection': IntersectionCommand,
        'kleene_closure': KleeneClosureCommand,
        'concatenation': CalculateConcatenationCommand,
        'power': CalculatePowerCommand,
        'inverse': CalculateInverseCommand,
        'cardinality': CalculateCardinalityCommand,
        'generate_languages': GenerateLanguagesCommand
    }

    def set_on_start(self, command: Command) -> None:
        self._on_start = command

    def set_on_finish(self, command: Command) -> None:
        self._on_finish = command

    def execute_action(self, action, values: list, *args):
        if action not in self.actions:
            print('Action not found')
            return False

        if isinstance(self._on_start, Command):
            self._on_start.execute()

        values.remove('#')
        action_result = self.actions[action](values, *args).execute()
        action_result.set_values(action_result.get_values().union({'#'}))

        if isinstance(self._on_finish, Command):
            on_finish = self._on_finish
            on_finish.set_result(action_result)
            on_finish.execute()

        return action_result
