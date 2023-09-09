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
        alphabet_a = symbols_a
        alphabet_b = symbols_b
        
        # Mostrar las listas
        typer.echo(f"List A : {alphabet_a}")
        typer.echo(f"List B : {alphabet_b}")

    else:
        typer.echo("Comando: python3 main.py" "nombre={elemento1,elemento2,...}" " nombre={elemento1,elemento2,...}")

if __name__ == "__main__":
    app()