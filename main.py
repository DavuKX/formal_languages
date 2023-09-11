import re
import typer
from src.commands.display_operation_result_command import DisplayOperationResultCommand
from src.commands.invoker import Invoker
from src.entities.alphabet import Alphabet


app = typer.Typer()

@app.command()

def input_data(alphabets: str):

    pattern = r'\s*(\w+)\s*=\s*{([^}]+)}'
    matches = re.findall(pattern, alphabets)
    formatted_alphabets = []

    for match in matches:
        alphabet_values = Alphabet(set(match[1].split(',')))
        formatted_alphabets.append(alphabet_values)

    invoker = Invoker()
    invoker.set_on_finish(DisplayOperationResultCommand())
    print("--------Alfabetos--------", end="\n\n")
    print(f'Union:')
    invoker.execute_action('union', formatted_alphabets)
    print()

    print(f'Interseccion:')
    invoker.execute_action('intersection', formatted_alphabets)
    print()

    print(f'Diferencia:')
    invoker.execute_action('difference', formatted_alphabets)
    print()
    words_number = int(input("Numero de palabras a generar para calcular cerradura de estrella:"))
    max_word_length = int(input("Cantidad de símbolos maximos de las palabras:"))
    print(f'Cerradura de estrella:')
    invoker.execute_action('kleene_closure', formatted_alphabets, words_number,max_word_length)

    print()
    print("--------Lenguajes--------", end="\n\n")
    words_number = int(input("Numero de palabras a generar de los lenguajes:"))
    max_word_length = int(input("Longitud maxima de las palabras:"))
    
    x = invoker.execute_action('kleene_closure', formatted_alphabets, words_number,max_word_length)

    invoker.execute_action('generate_languages',x,words_number,max_word_length)
    
    # invoker.execute_action('concatenation', formatted_alphabets)
    # invoker.execute_action('power', formatted_alphabets[0], power)
    # invoker.execute_action('inverse', formatted_alphabets[0])
    # invoker.execute_action('cardinality', formatted_alphabets[0])
    
if __name__ == "__main__":
    app()
