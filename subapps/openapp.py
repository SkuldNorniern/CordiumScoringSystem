import os
import typer
import subprocess as sbp
from core import configmod as cfm
from core import miscfuncmod as mfm

def openpbf(name):
    typer.echo("Opening Problem File")
    path = cfm.calldirdt(name)
    file = (mfm.rmwrongval(path)[1:]+"\\"+name+".pdf")
    sbp.Popen([file],shell=True)

def opendir(name):
    typer.echo("Opening Problem Directory")
    path = cfm.calldirdt(name)
    mfm.openfileexp(path)
