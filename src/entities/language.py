from src.entities.set_operations import SetOperations


class Language(SetOperations):
    def __init__(self, values: set):
        super().__init__(values)

    def concatenation(self, other_language):
        result_values = set()
        for value1 in self.get_values():
            for value2 in other_language.get_values():
                result_values.add(value1 + value2)
        return Language(result_values)

    def power(self, exponent):
        if exponent < 1:
            raise ValueError("Exponent must be positive")
        result = Language(self.get_values())
        for i in range(exponent - 1):
            new_result = Language(set())
            for word1 in result.get_values():
                for word2 in self.get_values():
                    new_result.get_values().add(word1 + word2)
            result = new_result
        return result

    def inverse(self):
        inverse_values = set()
        for word in self.get_values():
            inverse_values.add(word[::-1])
        return Language(inverse_values)

    def cardinality(self):
        return len(self.values)

