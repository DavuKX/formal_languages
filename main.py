<<<<<<< HEAD
import typer
from rich import print as rprint

app = typer.Typer()


@app.command("input_alphabets")
def sample_func():
    rprint("input_alphabets")


@app.command("union_alphabets")
def sample_func():
    rprint("[red bold]union_alphabets")


@app.command("diff_alphabets")
def sample_func():
    rprint("[red bold]diff_alphabets")


@app.command("intersect_alphabets")
def sample_func():
    rprint("[red bold]intersect_alphabets")


@app.command("alphabet_star_lock")
def sample_func():
    rprint("[red bold]alphabet_star_lock")


@app.command("generate_languages")
def sample_func():
    rprint("generate_languages")


@app.command("union_languages")
def sample_func():
    rprint("[red bold]union_languages")


@app.command("diff_languages")
def sample_func():
    rprint("[red bold]diff_languages")


@app.command("concat_languages")
def sample_func():
    rprint("[red bold]concat_languages")


@app.command("power_of_language")
def sample_func():
    rprint("[red bold]power_of_language")


@app.command("invert_language")
def sample_func():
    rprint("[red bold]invert_language")


@app.command("language_cardinality")
def sample_func():
    rprint("[red bold]language_cardinality")


if __name__ == "__main__":
    app()
=======
import sys
import re
import typer

app = typer.Typer()

def parse_set(input_str):
    #expresion regular para extraer el nombre del conjunto y los elementos, ignorando los espacios en blanco
    match = re.match(r'\s*(\w+)\s*=\s*{([^}]+)}', input_str)

    if match:
        # Extraemos los simbolos del conjunto 
        symbols_str = match.group(2)
        # Removemos espacios en blanco de los elementos para que no los tome como simbolos
        symbols = symbols_str.replace(" ", "").split(',')
        return symbols
    else:
        return None

@app.command()
def alphabet(a: str, b: str):
    symbols_a = parse_set(a)
    symbols_b = parse_set(b)

    if symbols_a is not None and symbols_b is not None:
        typer.echo(f"Alphabet A: {symbols_a}")
        typer.echo(f"Alphabet B: {symbols_b}")

        # Guardar los elementos en listas
        alphabet_a = set(symbols_a)
        alphabet_b = set(symbols_b)
        
        # Mostrar las listas
        typer.echo(f"List A : {alphabet_a}")
        typer.echo(f"List B : {alphabet_b}")

    else:
        typer.echo("Comando: python3 main.py" "nombre={elemento1,elemento2,...}" " nombre={elemento1,elemento2,...}")

if __name__ == "__main__":
    app()
>>>>>>> 7d555ec60566f77308e3fa1ae1f9e4a589a1fc2d
