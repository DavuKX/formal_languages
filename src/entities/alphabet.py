import copy

from src.entities.set_operations import SetOperations


class Alphabet(SetOperations):

    def concat(self, alphabet):
        result = set()
        for i in self.get_values():
            for j in alphabet.get_values():
                result.add(i + j)
        return Alphabet(result)

    def power(self, power):
        result = copy.deepcopy(self)
        for i in range(power - 1):
            result = result.union(result.concat(self).get_values())
        return result

    def generate_words_with_kleene_closure(self, words_number):
        current_word_count = len(self.values)

        if current_word_count >= words_number:
            print(1)
            selected_words = set(list(self.values)[:words_number])
            return Alphabet(selected_words)
        else:
            additional_words_needed = words_number - current_word_count
            power_value = (additional_words_needed // current_word_count) + 2
            new_alphabet = self.power(power_value)

            selected_words = set(list(new_alphabet.values)[:words_number])
            return Alphabet(selected_words)
