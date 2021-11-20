import os
import sys
import shutil
import platform as ptf
import subprocess as sbp
from core import loggermod as lgm

pathIron = r'C:\Program Files (x86)\IronPython 2.7\Lib'
sys.path.append(pathIron)

pathval = ".\/"

def rmpathval(name):
    for x in range(len(pathval)):
        name = name.replace(pathval[x],"")
    return name

def iscorrect(a,b):
    return a==b

def mkdir(name):
    os.makedirs(name)

def movefile(file,path):
    shutil.move(file, path)

def rmfile(file):
    os.remove(file)

def openfileexp(path):
    if ptf.system() == "Windows":
        os.startfile(path)
    elif ptf.system() == "Darwin":
        sbp.Popen(["open", path])
    else:
        sbp.Popen(["xdg-open", path])
    
