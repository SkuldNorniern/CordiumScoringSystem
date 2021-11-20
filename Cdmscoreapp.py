import os
import typer
from core import configmod as cfm
from core import loggermod as lgm
from subapps import initapp as iap
from subapps import testapp as tap
from subapps import openapp as oap
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

@app.command()
def open(name: str,
         flag: str = typer.Option("p","--f",help="--f f to open the folder, --f p to open the problem")):
    if(cfm.chkdirdt(name)): 
        if flag =="f":
            oap.opendir(name)
        else :
            oap.openpbf(name)
            
    
if __name__ == "__main__":
    app()