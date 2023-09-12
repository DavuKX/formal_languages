import re
import typer
from src.commands.display_operation_result_command import DisplayOperationResultCommand
from src.commands.invoker import Invoker
from src.entities.alphabet import Alphabet

app = typer.Typer()


@app.command()
def input_data(alphabets: str):
    check_input(alphabets)
    pattern = r'\s*(\w+)\s*=\s*{([^}]+)}'
    matches = re.findall(pattern, alphabets)
    formatted_alphabets = []

    for match in matches:
        alphabet_values = Alphabet(set(match[1].split(',')))
        formatted_alphabets.append(alphabet_values)

    invoker = Invoker()
    invoker.set_on_finish(DisplayOperationResultCommand())
    print("--------Alfabetos--------", end="\n\n")
    print(f'Unión:')
    invoker.execute_action('union', formatted_alphabets)
    print()

    print(f'Diferencia:')
    invoker.execute_action('difference', formatted_alphabets)
    print()

    print(f'Intersección:')
    invoker.execute_action('intersection', formatted_alphabets)
    print()

    words_number = int(input("Número de palabras a generar para calcular cerradura de estrella: "))
    max_word_length = int(input("Cantidad de símbolos máximos de las palabras: "))
    print(f'Cerradura de estrella:')

    kleened_closure_alphabet = invoker.execute_action('kleene_closure', formatted_alphabets, words_number,
                                                      max_word_length)

    print()
    print("--------Lenguajes--------", end="\n\n")
    words_number = int(input("Número de palabras a generar de los lenguajes: "))
    max_word_length = int(input("Longitud máxima de las palabras: "))

    language_1 = invoker.execute_action('generate_languages', kleened_closure_alphabet, words_number, max_word_length)
    language_2 = invoker.execute_action('generate_languages', kleened_closure_alphabet, words_number, max_word_length)
    languages = [language_1, language_2]

    print(f'Unión:')
    joined_languages = invoker.execute_action('union', languages)
    print()
    
    print(f'Diferencia:')
    invoker.execute_action('difference', languages)
    print()
    
    print(f'Interseccion:')
    invoker.execute_action('intersection', languages)
    print()
    
    print(f'Concatenación:')
    invoker.execute_action('concatenation', languages)
    print()
    
    power = int(input("Ingrese la potencia a calcular: "))
    print(f'Potencia:')
    invoker.execute_action('power', joined_languages, power)
    print()
    
    print(f'Inversa:')
    invoker.execute_action('inverse', joined_languages)
    print()
    
    print(f'Cardinalidad:')
    invoker.execute_action('cardinality', joined_languages)
    print()

def check_input(input_str: str):
    pattern_1 = r'#[^,}]'
    pattern_2 = r'[^,{]#'

    if re.search(pattern_1, input_str) or re.search(pattern_2, input_str):
        typer.echo("Error: Lambda no puede estar acompañado de otros símbolos.")
        raise typer.Exit()


if __name__ == "__main__":
    app()
