import os
import sys
import typer
import subprocess as sbp
from core import loggermod as lgm
from core import runnermod as rnm
from core import miscfuncmod as mfm

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
    
    name = mfm.rmpathval(name)
    typer.echo(f"The problem name is {name},The user name is {user}")
    res = rnm.compile(file,supported_language[ext],name,user)
    if res:print("맞았습니다.")
    else: print("틀렸습니다.")
    
