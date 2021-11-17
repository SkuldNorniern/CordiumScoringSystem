import os
import typer
import sys
import subprocess as sbp
from core import loggermod as lgm

supported_language={".py":"Python",".cpp":"C/C++",".c":"C/C++",".java":"Java"}
supported_extention=[".py",".c",".cpp",".java"]
compile_args={".py":"python",".java":"java"}

def tester(file):
    typer.echo(f"Given file is {file}")
    path,ext = os.path.splitext(file)
    name,user= path.split("-")
    if ext not in supported_extention:
        lgm.logmsg('Not Supported!','err')
    else:
        typer.echo(f"{supported_language[ext]} is Supported")
    typer.echo(f"The Name is {name},The user name is {user}, the extension is {ext}")
    compile(file,ext,name,user)

def compile(file,ext,name,user):
    typer.echo(f"{file}")
    #f = open("cache.dat", 'w')
    #cache = []
    #file_cache=[sys.executable,'-u','']
    process=sbp.Popen(f"{compile_args[ext]} {file}",stdout=sbp.PIPE,stderr=sbp.STDOUT,universal_newlines=True)
    #out = sbp.check_output(["ntpq", "-p"])
    #print(out)
    out, cmd_err = process.communicate()
    print(out)