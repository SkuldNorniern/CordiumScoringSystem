import subprocess as sbp
from core import loggermod as lgm

pathval = ".\/"

def rmpathval(name):
    for x in range(len(pathval)):
        name = name.replace(pathval[x],"")
    return name

def iscorrect(a,b):
    return a==b

def mkdir(name):
    sbp.run(f"mkdir {name}")

def movefile(file,path):
    sbp.run(f"move {file} {path}",shell=True)

def rmfile(file):
    sbp.run(f"rm {file}")