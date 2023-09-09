from abc import abstractmethod, ABC


class SetOperations(ABC):
    @abstractmethod
    def union(self, other):
        pass

    @abstractmethod
    def difference(self, other):
        pass

    @abstractmethod
    def intersection(self, other):
        pass
