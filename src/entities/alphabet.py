import random


from src.entities.set_operations import SetOperations

class Alphabet(SetOperations):

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
        return self.generate_words_with_kleene_closure(words_number, max_word_length)


    

    

    