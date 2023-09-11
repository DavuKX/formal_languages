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
    print(f'Union:')
    invoker.execute_action('union', formatted_alphabets)
    print(f'Interseccion:')
    invoker.execute_action('intersection', formatted_alphabets)
    print(f'Diferencia:')
    invoker.execute_action('difference', formatted_alphabets)

    words_number = int(input("Numero de palabras a generar para calcular cerradura de estrella:"))
    max_word_length = int(input("Longitud de las palabras:"))
    print(f'Cerradura de estrella:')
    invoker.execute_action('kleene_closure', formatted_alphabets, words_number,max_word_length)
    #invoker.execute_action('kleene_closure', formatted_alphabets, words_number, words_length)

if __name__ == "__main__":
    app()
