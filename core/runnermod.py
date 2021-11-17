import os
import sys
import typer
import subprocess as sbp

compile_args={"Python":"python","Java":"java","C/C++":"clang"}

def compile(file,lang,name,user):
    typer.echo(f"{file}")
    process=sbp.Popen(f"{compile_args[lang]} {file}",stdout=sbp.PIPE,stderr=sbp.STDOUT,universal_newlines=True)
    out, cmd_err = process.communicate()
    print(out)
    return out