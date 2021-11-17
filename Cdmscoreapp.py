import os
import typer
from core import loggermod as lgm
from subapps import initapp
from subapps import testapp
app = typer.Typer()
@app.command()
def init():
    typer.echo(f"Setting up Scoring space...")

@app.command()
def test(file: str):
    if not(os.path.exists(file)):
        lgm.logmsg('No File Detected !','err')
        return
    testapp.tester(file)

if __name__ == "__main__":
    app()