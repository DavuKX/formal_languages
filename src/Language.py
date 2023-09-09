from src.setOperations import SetOperations


class Language(SetOperations):
    def __init__(self, words):
        self.words = set(words)

    def union(self, other):
        if isinstance(other, Language):
            return Language(self.words.union(other.words))
        else:
            raise ValueError("Invalid operation: Union operation is only valid between languages.")

    def difference(self, other):
        if isinstance(other, Language):
            return Language(self.words.difference(other.words))
        else:
            raise ValueError("Invalid operation: Difference operation is only valid between languages.")

    def intersection(self, other):
        if isinstance(other, Language):
            return Language(self.words.intersection(other.words))
        else:
            raise ValueError("Invalid operation: Intersection operation is only valid between languages.")

    def concatenation(self, other):
        if isinstance(other, Language):
            new_words = [w1 + w2 for w1 in self.words for w2 in other.words]
            return Language(new_words)
        else:
            raise ValueError("Invalid operation: Concatenation operation is only valid between languages.")

    def power(self, n):
        if n == 0:
            return Language([""])
        elif n == 1:
            return self
        else:
            result = self
            for _ in range(n - 1):
                result = result.concatenation(self)
            return result

    def inverse(self):
        new_words = [word[::-1] for word in self.words]
        return Language(new_words)

    def cardinality(self):
        return len(self.words)