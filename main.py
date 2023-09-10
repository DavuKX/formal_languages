import re
import typer
from src.commands.display_operation_result_command import DisplayOperationResultCommand
from src.commands.invoker import Invoker
from src.entities.alphabet import Alphabet

app = typer.Typer()


@app.command()
def input_data(alphabets: str, words_number: int = 20):
    pattern = r'\s*(\w+)\s*=\s*{([^}]+)}'
    matches = re.findall(pattern, alphabets)
    formatted_alphabets = []

    for match in matches:
        alphabet_values = Alphabet(set(match[1].split(',')))
        formatted_alphabets.append(alphabet_values)

    invoker = Invoker()
    invoker.set_on_finish(DisplayOperationResultCommand())
    invoker.execute_action('union', formatted_alphabets)
    invoker.execute_action('difference', formatted_alphabets)
    invoker.execute_action('intersection', formatted_alphabets)
    invoker.execute_action('kleene_closure', formatted_alphabets, words_number)


if __name__ == "__main__":
    app()
