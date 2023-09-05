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
