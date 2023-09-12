import copy
import random

from src.entities.set_operations import SetOperations
from src.entities.language import Language


class Alphabet(SetOperations):

    # def concat(self, alphabet):
    #     result = set()
    #     for i in self.get_values():
    #         for j in alphabet.get_values():
    #             result.add(i + j)
    #     return Alphabet(result)

    # def power(self, power):
    #     result = copy.deepcopy(self)
    #     for i in range(power - 1):
    #         result = result.union(result.concat(self).get_values())
    #     return result
        
    def validate_lambda(self):
        pass

    def generate_words_with_kleene_closure(self, words_number, max_word_length):
        generated_words = set()
        is_lambda = 0
        while len(generated_words) < words_number:
            random_word_length = random.randint(1, max_word_length)
            random_word = ''.join(random.choice(list(self.values)) for _ in range(random_word_length))
            if '#' in random_word:
                if random_word == '#' and is_lambda == 0:
                    generated_words.add(random_word)
                    is_lambda+=1
            else:
                generated_words.add(random_word)

        return Alphabet(generated_words)
    
    def generate_language(self, words_number, max_word_length):
        # languages = set()
        # languages = self.generate_words_with_kleene_closure(words_number, max_word_length)
        # language_b = self.generate_words_with_kleene_closure(words_number, max_word_length)
        #languages.add(language_a)
        # languages.add(language_b)
        return self.generate_words_with_kleene_closure(words_number, max_word_length)


    

    

    