import os
import sys
import typer
import subprocess as sbp
from core import loggermod as lgm
from core import runnermod as rnm

supported_language={".py":"Python",".cpp":"C/C++",".c":"C/C++",".java":"Java"}
supported_extention=[".py",".c",".cpp",".java"]


def tester(file):
    typer.echo(f"Given file is {file}")
    path,ext = os.path.splitext(file)
    name,user= path.split("-")
    if ext not in supported_extention:
        lgm.logmsg('Not Supported!','err')
    else:
        typer.echo(f"{supported_language[ext]} is Supported")
    typer.echo(f"The name is {name},The user name is {user}, the extension is {ext}")
    res = rnm.compile(file,supported_language[ext],name,user)

