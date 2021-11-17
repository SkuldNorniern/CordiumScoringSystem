import os
import typer
from core import loggermod as lgm
from subapps import initapp as iap
from subapps import testapp as tap
app = typer.Typer()
@app.command()
def init(name: str, timeout: int, datacnt: int, path: str):
    typer.echo(f"Setting up Scoring space...")
    iap.init(name, timeout, datacnt, path)


@app.command()
def test(file: str):
    if not(os.path.exists(file)):
        lgm.logmsg('No File Detected !','err')
        return
    tap.tester(file)

if __name__ == "__main__":
    app()