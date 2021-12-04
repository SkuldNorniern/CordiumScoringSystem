import os
import sys
import shutil
import platform as ptf
import subprocess as sbp
from core import loggermod as lgm

pathIron = r'C:\Program Files (x86)\IronPython 2.7\Lib'
sys.path.append(pathIron)

pathval = ".\/"
wrongval = "."
CREATE_NO_WINDOW = 0x08000000

def rmpathval(name):
    for x in range(len(pathval)):
        name = name.replace(pathval[x],"")
    return name

def rmwrongval(path):
    for x in range(len(wrongval)):
        path = path.replace(wrongval[x], "")
    return path

def iscorrect(a,b):
    return a==b

def mkdir(name):
    os.makedirs(name)

def movefile(file,path):
    shutil.move(file, path)

def rmfile(file):
    try:
       os.remove(file)
    except Exception:
        sbp.call('taskkill /F /IM '+file, creationflags=CREATE_NO_WINDOW)
        os.remove(file)
    except:
        pass


def openfileexp(path):
    path = rmwrongval(path)[1:]
    if ptf.system() == "Windows":
        os.startfile(path)
    elif ptf.system() == "Darwin":
        sbp.Popen(["open", path])
    else:
        sbp.Popen(["xdg-open", path])
    
