from abc import ABC, abstractmethod

class Command(ABC):

    @abstractmethod
    def execute(self) -> set:
        pass

    def set_result(self, action_result):
        pass

    def get_result(self):
        pass
