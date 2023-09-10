from src.commands.command import Command
from src.commands.difference_command import DifferenceCommand
from src.commands.intersection_command import IntersectionCommand
from src.commands.kleene_closure_command import KleeneClosureCommand
from src.commands.union_command import UnionCommand


class Invoker:
    _on_start = None
    _on_finish = None
    actions = {
        'union': UnionCommand,
        'difference': DifferenceCommand,
        'intersection': IntersectionCommand,
        'kleene_closure': KleeneClosureCommand
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

        action_result = self.actions[action](values, *args).execute()

        if isinstance(self._on_finish, Command):
            on_finish = self._on_finish
            on_finish.set_result(action_result)
            on_finish.execute()

        return action_result
