class SetOperations:
    def __init__(self, values: set):
        self.values = values

    def set_values(self, values: set):
        self.values = values
        return self

    def get_values(self):
        return self.values

    def union(self, set2: set):
        self.values = self.values.union(set2)
        return self

    def intersection(self, set2: set):
        self.values = self.values.intersection(set2)
        return self

    def difference(self, set2: set):
        self.values = self.values.difference(set2)
        return self

    